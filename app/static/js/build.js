const tiles = document.querySelectorAll('.tile')
const display = document.querySelector('#display')
const playerInfo = document.querySelector('#player_info')
{
    const buildInput = document.querySelector('#build_input')

    tiles.forEach(tile => tile.addEventListener('click', e => {
        if (e.target.dataset.owner_id === playerInfo.dataset.current_player_index) {
            if (parseInt(e.target.dataset.build_price, 10) < parseInt(playerInfo.dataset.current_player_money, 10)) {
                if (e.target.dataset.build != 'h') {
                    buildInput.value += e.target.dataset.id + ';'
                    e.target.style = 'border: 3px solid blue'
                }
            }
        }

    }))
}
{
    tiles.forEach(tile => {
        tile.addEventListener('mouseenter', e => {
            const text = e.target.textContent
            // console.log(text)
        })

        tile.addEventListener('mouseout', () => {
            // console.log('out')
        })
    })
}