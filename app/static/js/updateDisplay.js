{
    const fetchFieldInfo = e => {
        const id = e.target.dataset.id
            const url = `/field_info/${id}`
            fetch(url)
                .then(blob => blob.json())
                .then(json => console.log(json))
                .catch(err => console.log(err))
    }

    tiles.forEach(tile => {
        tile.addEventListener('mouseenter', throttle(fetchFieldInfo, 700))

        tile.addEventListener('mouseout', () => {
            // console.log('out')
        })
    })
}