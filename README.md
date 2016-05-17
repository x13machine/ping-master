# ping-master

The key needs to be changed manually in the source code to something secret to prevent people from hacking the server.

The protocol is as follows:

If `$KEY PING $SERVER` is sent, `$KEY PONG` is returned, and the $SERVER value will be stored.

If `$KEY PING` is sent, `$KEY PONG` is returned and the IP address will be stored.

If `$KEY LS` is sent, a list of servers (e.g. `$KEY LS SERVER1 SERVER2 SERVER3 ...`) is returned.
