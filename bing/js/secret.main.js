async function updateLoteryData(Lid, values) {
    const response = await fetch('/api/?table=Last_lotery&query=put', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            Lid: Lid,
            values: values
        })
    });

    if (!response.ok) {
        throw new Error('Network response was not ok');
    }

    const data = await response.json();
    console.log(data);
}

async function addLoteryData(values) {
    console.log(values);
    const response = await fetch('/api/?table=Last_lotery&query=add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            values: values
        })
    });

    if (!response.ok) {
        throw new Error('Network response was not ok');
    }

    const data = await response.json();
    console.log(data);
}
