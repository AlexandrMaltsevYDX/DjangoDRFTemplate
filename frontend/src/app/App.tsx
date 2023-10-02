import React, { useState, useEffect } from "react";
import "./App.scss";
import { Card } from "react-bootstrap";

function App() {
    const API_URL = "http://localhost/api/cards/";

    const [items, setItems] = useState([]);

    useEffect(() => {
        const fetchItems = async () => {
            const response = await fetch(API_URL);
            if (!response.ok) throw Error("Did not receive expected data");
            const listItems = await response.json();
            setItems(listItems);
        };

        setTimeout(() => fetchItems(), 2000);
    }, []);

    return (
        <>
            {items.map((card, index) => (
                <Card key={index}>
                    <Card.Body>
                        <Card.Title>{card.name}</Card.Title>
                        <Card.Text>{card.image}</Card.Text>
                    </Card.Body>
                </Card>
            ))}
        </>
    );
}

export default App;
