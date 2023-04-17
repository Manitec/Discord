# Discord

Create Servers, Channels, Direct Messages and more! Built using Python and React.js.

[Discord!][live]

[Features | Redux Store][wiki-features]

[API Routes][wiki-routes]

[Database Schema][wiki-db-schema]

[live]: https://discord-wa36.onrender.com
[wiki-routes]:https://github.com/CheadleCheadle/Discord/wiki/API-Routes
[wiki-features]:https://github.com/CheadleCheadle/Discord/wiki/Redux-Store-Shape-&-Feature-List
[wiki-db-schema]:https://github.com/CheadleCheadle/Discord/wiki/Database-Design

## Main Features

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

## To-do
 * Implement create and delete for friendships
 * Implement search for servers and users
 * Implement server roles
 
 ## To launch the application locally:
 * Clone the repository
 * Open the root folder and type "pipenv install" to install dependencies
 * Open the frontend folder called 'react-app' and type "npm install"
 * In the root folder, type "pipenv run flask run" to start the flask server on localhost:5000
 * Inside the 'react-app' folder type "npm start" to start the react frontend server on localhost:3000
 * The application should now be running!
## Screenshot
![new](https://user-images.githubusercontent.com/108553712/232428796-732b1da7-079c-4595-8e2c-e3b27355d90c.PNG)
If you wish to stop using the application, you can close it by hitting ctrl + c inside of both the root and frontend folders.
