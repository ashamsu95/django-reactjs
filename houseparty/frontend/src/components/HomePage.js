import React, {Component} from "react";
import CreateRoomPage from "./CreateRoomPage";
import RoomJoinPage from "./RoomJoinPage";
import Room from "./Room";
import {BrowserRouter as Router,Switch,Route,Link,Redirect} from "react-router-dom"

export default class HomePage extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return <Router>
            <switch>
                <Route exact path='/'><p>Loraitsum</p></Route>
                <Route path='/join' component={RoomJoinPage}/>
                <Route path='/create' component={CreateRoomPage} />
                <Route path='/room/:roomcode' component={Room}/>
            </switch>
        </Router>;
    }
}