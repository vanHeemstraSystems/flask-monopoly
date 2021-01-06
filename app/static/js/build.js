const tiles = document.querySelectorAll('.tile')
const display = document.querySelector('#display')
const playerInfo = document.querySelector('#player_info')
{
    const buildInput = document.querySelector('#build_input')

    tiles.forEach(tile => tile.addEventListener('click', e => {
        if (e.target.dataset.owner_id === playerInfo.dataset.current_player_index) {
            console.log('własne')
            if (parseInt(e.target.dataset.build_price, 10) < parseInt(playerInfo.dataset.current_player_money, 10)) {
                console.log('stać')
                if (e.target.dataset.build != 'h') {
                    console.log('jeszcze')
                    buildInput.value += e.target.dataset.id + ';'
                    e.target.style = 'border: 1px solid red'
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