{
    const tiles = document.querySelectorAll('.tile')
    const display = document.querySelector('#display')

    tiles.forEach(tile=>{
        tile.addEventListener('mouseenter', e=>{
            const text = e.target.textContent
            display.textContent = text
        })
        
        tile.addEventListener('mouseout', ()=>{
            display.textContent = ''
        })
    })
}