{
    const tiles = document.querySelectorAll('.tile')
    const display = document.querySelector('#display')

    tiles.forEach(tile=>{
        tile.addEventListener('mouseenter', e=>{
            const text = e.target.textContent
            console.log(text)
        })
        
        tile.addEventListener('mouseout', ()=>{
            console.log('out')
        })
    })
}