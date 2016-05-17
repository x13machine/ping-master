# ping-master

the key needs to be changed manually in the source code to something sercet to prevent people from hacking the server.

the protocal goes like this

If you send.
```
$KEY PING $SERVER
```

You will get:

```
$KEY PONG
```

the $SERVER value will be stored

If you send.
```
$KEY PING
```

You will get:

```
$KEY PONG
```

the ip address will be stored

If you send.
```
$KEY LS
```

You will get:

```
$KEY LS SERVER1 SERVER2 SERVER3 ...
```

LS will return the list of servers
