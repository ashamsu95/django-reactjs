import React,{ Component } from 'react';

export default class Room extends Component{
    constructor(props){
        super(props);
        this.state={
            votesToSkip:2,
            guestCanPause:false,
            isHost:false,
        };
        this.roomCode = this.props.match.params.roomcode
        this.getRoomDetails();
    }

    getRoomDetails(){
        fetch('/api/get-room'+ '?code=' + this.roomCode)
        .then((response)=> response.json())
        .then((data) => {
            this.setState({
                votesToSkip: data.votes_to_skip,
                guestCanPause:data.guest_can_pause,
                isHost: data.is_host,
            });
        });
    }

    render(){
        return( 
        <div>
            <h3>{this.roomCode}</h3>
            <p>Vote:{this.state.votesToSkip.toString()}</p>
            <p>Guest can Pause:{this.state.guestCanPause.toString()}</p>
            <p>Host:{this.state.isHost.toString()}</p>
        </div>
        );
    }
}