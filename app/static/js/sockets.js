{
    const socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    const room = playerInfo.dataset.code
    socket.emit('join', {room})

    socket.on('refresh', data=>{
        const curr_id = parseInt(playerInfo.dataset.current_db_id, 10)
        if(curr_id === data.last_player){
            location.reload()
        }

    })
}