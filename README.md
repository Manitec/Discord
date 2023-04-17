# Discord

Create Servers, Channels, Direct Messages and more! Built using Python and React.js.

[Discord!][live]

[live]: https://discord-wa36.onrender.com

## Features

This Discord clone utilizes flask-socketio as well as the socket-io package from Javascript
to render messages between clients in real time! Additionally, it allows for creating, updating and deleting both servers
and channels as well as server memberships.

## WebSocket Implementation
```
  const sendMessagesThunk = () => async (dispatch) => {
    const newMessage = { content: messageText, userId: user.id };
    const response = await fetch(`/api/users/messages/new/${friend.id}`, {
      method: "POST",
      headers: { "Content-Type": "Application/json" },
      body: JSON.stringify(newMessage),
    });
    if (response.ok) {
      const data = await response.json();
      const charCode2 = charCode(username, friendname)
      socket.emit("message", { username, friendname, message: data, charCode2 });
      setMessageText("");
    }
  }

  const charCode = (username, friendname) => {
    let sum = 0;
    let unique = username.concat(friendname)
    for (let i = 0; i < unique.length; i++) { sum += unique.charCodeAt(i) }
    return sum;
  }

  useEffect(() => {
    dispatch(fetchMessagesThunk(friend.id))
      .then((res) => setMessages(res))
      .then(() => setIsLoaded(true))
    // Join the chat room when the component mounts
    const charCode2 = charCode(username, friendname)
    setRoomName(charCode2);
    socket.emit("join", { username, friendname, charCode2 });

    // Handle incoming messages
    socket.on("new_message", (data) => {
      setMessages((messages) => [ ...messages, data.message ]);
    });

    // Leave the chat room when the component unmounts
    return () => {

      const charCode2 = charCode(username, friendname)
      socket.emit("leave", { username, friendname, charCode2 });
    };
  }, [ friendname ]);
end
```
(full websocket implementation can be found in /components/DirectMessages)

## Front End

- Uses React.js
- Implements Redux for state management
- Uses RESTful requests to query Flask


## Screenshot![splash-page](https://user-images.githubusercontent.com/108553712/232428462-37d01bf4-8b6f-48c7-9ef9-bc63efb08c8f.PNG)

