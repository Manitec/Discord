import { useParams } from "react-router-dom";
import { useCallback, useEffect, useMemo, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import "./main.css"
import { filter } from "lodash";
import { changeMembershipStatusThunk } from "../../../store/session";
export default function Members() {
 const history = useHistory();
 const params = useParams();
 const dispatch = useDispatch();
 const serverId = useSelector(state => state.servers.singleServerId)
 const [isLoaded, setIsLoaded] = useState(false);
 const members = useSelector(
  (state) => state.servers.allServers[state.servers.singleServerId].users
 );
 const memberships = useSelector(state => state.session.user.servers[state.servers.singleServerId].memberships);

 console.log("IM THE MEMBERSHIPS!", memberships);
 console.log("IM THE MEMBERS!", members);

 const handleAccept = (member) => {
    dispatch(changeMembershipStatusThunk(serverId, member.id ))
 }

const filterMembers = (type) => {
    if (memberships) {
        const filtered = members.filter(member => {
            if (memberships[member.id].status === type) {
                return true
            }
        })
        console.log("FILTERED", filtered, type);
        return filtered
    }
    return [];
}
useEffect(() => {
    setIsLoaded(true)
}, [memberships])

 return ( isLoaded &&
    <div className="members-cont">

    <span id="status">Host - 1</span>
    {filterMembers("Host").map((member) => (
     <div id="members-info"key={member.id}>
      <div id ="mbr-image">
       <img src={member.photo_url}></img>
      </div>
      <p>{member.username}</p>
     </div>
    ))}
    {filterMembers("Member").length ? <span id="status">Members - {filterMembers("Member").length}</span> : null}
    {filterMembers("Member").map((member) => (
     <div id="members-info" key={member.id}>
      <div id="mbr-image">
       <img src={member.photo_url}></img>
      </div>
      <p>{member.username}</p>
     </div>
    ))}
    {filterMembers("Pending").length ? <span id="status">Pending - {filterMembers("Pending").length}</span> : null}
    {filterMembers("Pending").map((member) => (
     <div id="members-info" key={member.id}>
      <div id="mbr-image">
       <img src={member.photo_url}></img>
      </div>
      <p>{member.username}</p>
      <button onClick={() => handleAccept(member)} id="accept-button">Accept?</button>
     </div>
    ))}
   </div>

 );
}
