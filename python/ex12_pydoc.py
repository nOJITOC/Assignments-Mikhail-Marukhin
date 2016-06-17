 raw_input([prompt]) -> string

 Read a string from standard input.  The trailing newline is stripped.
 If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
 On Unix, GNU readline is used if enabled.  The prompt string, if given,
 is printed without a trailing newline before reading.
 open(...)
    open(name[, mode[, buffering]]) -> file object

    Open a file using the file() type, returns a file object.  This is the
    preferred way to open a file.  See file.__doc__ for further information.
	
 
 В-четвёртых, утилита pydoc даёт возможность просматривать описание модулей:

c:/python/lib/pydoc.py mytest.py
1
	
c:/python/lib/pydoc.py mytest.py

В-пятых, несложно с помощью pydoc запустить сервис и читать документацию в браузере:

c:/python/lib/pydoc.py -p 8088
1
	
c:/python/lib/pydoc.py -p 8088

Документация будет доступна на http://127.0.0.1:8088/.