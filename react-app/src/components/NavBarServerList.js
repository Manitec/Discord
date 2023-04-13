import NavBarServer from "./NavBarServer";
import AddChannelModal from "./AddChannelModal/index";
import OpenModalMenuItem from "./OpenModalButton/";
import Server from "../components/ServerDetails/index.js";
import { NavLink, useHistory } from "react-router-dom";
import "./Navigation/Navigation.css"
import { useSelector } from "react-redux";
function NavBarServerList() {
  const serversObj = useSelector(state => state.session.user.servers)
  const servers = Object.values(serversObj)
  const history = useHistory();

  return (
    <>
      {servers.map((server) => (
        <NavLink to={`/servers/${server.id}`}>
          <div key={server.id} className="svr-nav-menu-item svr-dropdown-parent">
            <NavBarServer server={server} />
          </div>
        </NavLink >
      ))}
      <div className="svr-channel-nav-bar-container">
        <div></div>
      </div>
    </>
  );
}

export default NavBarServerList;
