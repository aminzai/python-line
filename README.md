# Line Messaging API for Python

A lot of todo....


# Exampe:

```
client = Client(
        channel_access_token='<TOKEN>'  # noqa 
        )
uid = '<UID>'
m = TextMessage("Hello, World!")
client.send_msg(uid, m)
```

