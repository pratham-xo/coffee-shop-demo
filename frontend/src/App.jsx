import { useEffect, useState } from "react";


function App() {

    const [products, setProducts] = useState([]);
    const [message, setMessage] = useState("");


    useEffect(() => {

        fetch("/api/products")
            .then(response => response.json())
            .then(data => setProducts(data))
            .catch(error => {
                console.error("Failed to load products:", error);
            });

    }, []);


    const placeOrder = async (productId) => {

        const response = await fetch("/api/orders", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                product_id: productId,
                quantity: 1
            })
        });

        const data = await response.json();

        if (response.ok) {
            setMessage(
                `Order placed successfully! Order ID: ${data.order_id}`
            );
        } else {
            setMessage(data.error);
        }
    };


    return (
        <div className="container">

            <h1>☕ Coffee Shop</h1>

            <p className="subtitle">
                Fresh coffee, delivered with code.
            </p>

            <div className="products">

                {products.map(product => (

                    <div
                        className="product-card"
                        key={product.id}
                    >

                        <h2>{product.name}</h2>

                        <p>
                            ₹{product.price}
                        </p>

                        <button
                            onClick={() => placeOrder(product.id)}
                        >
                            Place Order
                        </button>

                    </div>

                ))}

            </div>

            {message && (
                <div className="message">
                    {message}
                </div>
            )}

        </div>
    );
}


export default App;
