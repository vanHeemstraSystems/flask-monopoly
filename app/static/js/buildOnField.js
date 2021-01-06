{
    const buildInput = document.querySelector('#build_input')

    tiles.forEach(tile => tile.addEventListener('click', e => {
        if (e.target.dataset.owner_id === playerInfo.dataset.current_player_index) {
            if (e.target.dataset.build_price < playerInfo.dataset.current_player_money) {
                if(e.target.dataset.build != 'h'){
                    buildInput.value += e.target.dataset.id+';'
                    e.target.style = 'border: 1px solid red'
                }
            }
        }

    }))
}