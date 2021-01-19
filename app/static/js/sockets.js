{
    const socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    const room = playerInfo.dataset.code
    socket.emit('join', {room})

    socket.on('refresh', data=>{
        console.log(reload)
        const curr_id = playerInfo.dataset.current_db_id
        if(curr_id != data.last_player){
            location.reload()
        }
    })
}