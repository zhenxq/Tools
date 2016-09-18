

# Android 
我们能修改的只是smali文件，通过写该samli文件然后重新编译为.dex文件。<br>
对于class.dex文件我们可以通过dex2jar将其转化为.jar，然后通过jd-gui.exe读取伪代码.<br>
class.dex <--> smali  <br>
class.dex <--> .jar(包含多个.class) <--> java(伪代码) <br>
## dex2jar
>https://sourceforge.net/p/dex2jar/wiki/Faq/#markdown-header-want-to-read-dex-file-using-dex2jar　<br>
dex2jar is a tool for converting Android's .dex format to Java's .class format. just one binary format to another binary format, not to source. <br>

获得smali和将smali重新编译为.dex文件(功能函数和smali/baksmali相同):<br>
d2j-smali/d2j-baksmali have the same function with smali/baksmali.<br>
command: <br/><pre>
    * dexd2j-baksmali.sh: .dex转换为smali
        dexd2j-baksmali.sh abc.apk       -- Linux disassemble the dex to smali files(dex转化为smali文件)
        d2j-baksmali.bat abc.apk         -- windows
    * d2j-smali.sh: smali转换为.dex
        d2j-smali.sh out -o classes.dex  -- assemble smali files to dex(smalie文件转换为dex)
        d2j-smali.bat out  -o ../class.dex --windows
</pre>
1. 解压apk，找到classes.dex（可能有多个不同类型的classes.dex）
2. 用dex2jar-2.0处理:
	帮助:d2j-dex2jar.bat -h
		-o,--output <out-jar-file>   output .jar file, default is $current_dir/[file-name]-dex2jar.jar（注意以-dex2jar.jar结尾）
command:<br/><pre>
    * d2j-dex2jar:.dex 转换为.jar
        d2j-dex2jar.bat classes.dex（路径） -o (保存的文件的路径./test/3-dex2jar.jar)，如果没有保存的文件的路径将会在本地生成文件。
    * d2j-jar2dex:.jar转换为 .dex
        d2j-jar2dex.sh --output=classes.dex abc.jar
        dx --dex --output=classes.dex abc.jar  (the dx tool from android sdk can do the job)
    * apktool if framework-res.apk                --------加载资源（install framework） 
</pre>
3. 通过jd工具进行Java Decompiler 获得java代码.

## smali/baksmali
> https://github.com/JesusFreke/smali/wiki<br>
   baksmali:classe.dex-->smali<br>
   smali:smali --> class.dex
   
command:<br><pre>
    baksmali: .dex转换为smali
        java -jar baksmali-2.1.3.jar weixin_861_1.apk  （没有指定samli输出文件夹会自动创建out文件夹）
        java -jar baksmali-2.1.3.jar classes.dex -o a/ （指定输出smali文件夹）
    smali: smali转换为.dex  (classes.dex放回.apk下覆盖原来的classes.dex文件。)
        java -jar smali-2.1.3.jar a/
        java -jar smali-2.1.3.jar a/ -o class.dex 
    </pre>

## Apktools
> https://ibotpeaches.github.io/Apktool/<br>

command:<pre>
    反编译：apktool d test.apk -o test(反编译后的文件路径) ；-f 参数是强制覆盖已经存在的文件。
    修改后的文件重新编译:   apktool b test
</pre>
APKTool是GOOGLE提供的APK编译工具，需要JAVA运行环境。



### 自动化工具：Android-killer<br>
GET smali tools:smali/baksmali,asmdex,dexmaker, they are excellent tools work with dex/odex directly

# 签名
1. Android使用标准的java工具 Keytool 、Jarsigner 来生成数字证书，并给应用程序包签名。
2. APK实际上是一个jar或者说是一个zip压缩文件，META-INF目录(解压.apk获得)下存放的是压缩包中所有文件的签名信息，用来保证apk包的完整性和系统的安全。
3. 重签名：实际上就是删除META-INF目录(删除已有签名)，使用自已数据证书再次重签名。
4. 注：APK如有签名自校验(代码有校验)需要修改其代码

工具：
JAVA自带工具：
    1. 数字证书生成：keytool
    2. 重新签名：jarsigner
  Android SDK自带工具:
    1. 优化APK：zipalign
      keytool -printcert -file *.RSA 打印证书信息

    生成证书:
      keytool -genkey -v -keystore debug.keystore -alias androiddebugkey -keyalg RSA -validity 10000
        1. keytool是工具名称；
        2. -genkey生成数字证书；
        3. -v表示将生成证书的详细信息打印出来，显示在dos窗口中； 
        4. -keystore  debug.keystore 生成的数字证书的---文件名为debug.keystore；
        5. -alias  androiddebugkey   表示证书的别名为androiddebugkey，可以与Keystore一样；
        6. -keyalg RSA 表示生成密钥文件所采用的算法为RSA；
        7. -validity 10000 表示该数字证书的有效期为10000天，意味着10000天之后该证书将失效。
    删除apk中的META-INF以前的签名文件：
    1. 解压.apk，删除META-INF
    2.在解压的文件内部进行打包为.zip(如果在外部进行打包会出现二级目录)
    3.将.zip文件剪切出来，更改为.apk
    重新进行apk签名：
    jarsigner -verbose -keystore debug.keystore -storepass android -keypass android -signedjar test_signed.apk  test_temp.apk androiddebugkey
    1. jarsigner是Java的签名工具
    2. -verbose参数表示：显示出签名详细信息
    3. -keystore表示使用当前目录中的debug.keystore签名证书文件。
    4. -storepass 密钥口令 (在生成证书的时候设置的值)
    5. -signedjar ThinkDrive_signed.apk表示签名后生成的APK名称，
    6. test_temp.apk 表示未签名的APK，
    7. androiddebugkey表示debug.keystore的别名
