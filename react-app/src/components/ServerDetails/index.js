import { useParams } from "react-router-dom"
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import "./Server.css";
import { loadServerChannel, loadServerChannels } from "../../store/channels.js"
import { thunkLoadAllServers } from "../../store/servers";
import Channel from "../ChannelDetails/index.js";
export default function Server({ sessionUser }) {
    const history = useHistory();
    const params = useParams();
    const dispatch = useDispatch();
    let { serverId } = params;
    serverId = parseInt(serverId);
    const server = useSelector(state => state.servers.allServers[ serverId ]);
    let currentChannel = useSelector(state => state.channels.allChannels[ state.channels.singleChannelId ]);

    const loadChannel = (channel) => {
        dispatch(loadServerChannel(channel))
        currentChannel = channel

    }

    useEffect(() => {
        dispatch(loadServerChannels({ channels: server.channels }))
        dispatch(loadServerChannel(server.channels[ 0 ]))

    }, [ server ])
    //Make sure in the future to make sure that this dispatch fires somewhere else. Probs in nav files
    useEffect(() => {
        dispatch(thunkLoadAllServers());
    }, [])
    return (

        <>
            <div className="svr-channel-wrapper">
                <div>
                    {server?.channels.map((channel) => (
                        <div key={channel.id} onClick={() => loadChannel(channel)}>
                            {channel.name}
                        </div>
                    ))}
                </div>
                <div className="svr-channel-msgs">
                    <Channel channel={currentChannel} />

                </div>




                <div>
                    {server?.users.map((user) => (
                        <div key={user.id}>
                            {user.username}
                            {user.photo_url}
                        </div>
                    ))}
                </div>

            </div>
        </>




    )

}
