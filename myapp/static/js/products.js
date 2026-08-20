// ---------------------- PRODUCT DATA ----------------------
const allProducts = [
    { id: 1, name: "Apple iPhone 14", price: "रु99,999", image: "https://images.unsplash.com/photo-1661447117654-5d8a2b2a0b6f" },
    { id: 2, name: "MacBook Pro 16", price: "रु299,999", image: "https://images.unsplash.com/photo-1517336714731-489689fd1ca8" },
    { id: 3, name: "Sony WH-1000XM5 Headphones", price: "रु49,999", image: "https://images.unsplash.com/photo-1591122332193-d7b7d36ef2b8" },
    { id: 4, name: "Samsung Galaxy S23", price: "रु109,999", image: "https://images.unsplash.com/photo-1677184638217-9b29f27f4ec7" },
    { id: 5, name: "Nike Air Max 270", price: "रु19,999", image: "https://images.unsplash.com/photo-1612461234519-4d57b5f88f44" },
    { id: 6, name: "Adidas Ultraboost", price: "रु21,999", image: "https://images.unsplash.com/photo-1600180758895-d6b1a8f7e798" },
    { id: 7, name: "Dell XPS 13 Laptop", price: "रु149,999", image: "https://images.unsplash.com/photo-1580910051070-15f8e3d83c68" },
    { id: 8, name: "Canon EOS R5 Camera", price: "रु439,999", image: "https://images.unsplash.com/photo-1606813909395-cb489fe22d9a" },
    { id: 9, name: "Logitech MX Master 3", price: "रु11,999", image: "https://images.unsplash.com/photo-1615559601203-0d2232baf47b" },
    { id: 10, name: "Amazon Echo Dot 5th Gen", price: "रु5,999", image: "https://images.unsplash.com/photo-1598332901093-9f8d30f93f0d" },
    { id: 11, name: "PlayStation 5", price: "रु69,999", image: "https://images.unsplash.com/photo-1606819054492-145ba45a2a65" },
    { id: 12, name: "Xbox Series X", price: "रु69,999", image: "https://images.unsplash.com/photo-1615393567302-b2b0f9aa9476" },
    { id: 13, name: "Kindle Paperwhite", price: "रु14,999", image: "https://images.unsplash.com/photo-1605708904505-7e3f9c805e48" },
    { id: 14, name: "GoPro Hero 10", price: "रु49,999", image: "https://images.unsplash.com/photo-1624287550047-79d78008f29e" },
    { id: 15, name: "Apple Watch Series 8", price: "रु49,999", image: "https://images.unsplash.com/photo-1661425561647-84d2c56d2fae" },
    { id: 16, name: "Samsung Galaxy Watch 5", price: "रु39,999", image: "https://images.unsplash.com/photo-1665683796394-5a8c7e7f9f44" },
    { id: 17, name: "Bose QuietComfort 45", price: "रु39,999", image: "https://images.unsplash.com/photo-1585386959984-a415522c2f1f" },
    { id: 18, name: "Microsoft Surface Laptop 5", price: "रु149,999", image: "https://images.unsplash.com/photo-1654784942337-08de8dff6bc1" },
    { id: 19, name: "iPad Pro 12.9", price: "रु109,999", image: "https://images.unsplash.com/photo-1592194996308-7b43878e84a6" },
    { id: 20, name: "HP Spectre x360", price: "रु119,999", image: "https://images.unsplash.com/photo-1614373611760-8b70b9e7b5e1" },
    { id: 21, name: "Faber-Castell Pen Set", price: "रु2,499", image: "https://images.unsplash.com/photo-1612831666354-d0f4e1959f6a" },
    { id: 22, name: "Montblanc Pen", price: "रु12,999", image: "https://images.unsplash.com/photo-1584282019365-5b1e49d72a5e" },
    { id: 23, name: "Reebok Running Shoes", price: "रु17,999", image: "https://images.unsplash.com/photo-1598970434795-0c54fe7c0642" },
    { id: 24, name: "Canon EOS M50", price: "रु79,999", image: "https://images.unsplash.com/photo-1589739907740-29b693fb0dc0" },
    { id: 25, name: "Samsung Galaxy Buds 2", price: "रु7,999", image: "https://images.unsplash.com/photo-1640337744328-1a5a5d8aefaa" },
    { id: 26, name: "Apple AirPods Pro", price: "रु24,999", image: "https://images.unsplash.com/photo-1585386959977-2e4efc99b1ea" },
    { id: 27, name: "HP Omen 16 Gaming Laptop", price: "रु149,999", image: "https://images.unsplash.com/photo-1600180758925-d6b1a8f7e799" },
    { id: 28, name: "Asus ROG Zephyrus G14", price: "रु199,999", image: "https://images.unsplash.com/photo-1600180758895-d6b1a8f7e799" },
    { id: 29, name: "Xiaomi Redmi Note 12", price: "रु29,999", image: "https://images.unsplash.com/photo-1630697229227-23b1f1f3b7c6" },
    { id: 30, name: "OnePlus 11", price: "रु79,999", image: "https://images.unsplash.com/photo-1676887042781-2c0c8c6df5b2" },
    { id: 31, name: "Logitech G502 Mouse", price: "रु5,499", image: "https://images.unsplash.com/photo-1623924263996-c8e33c4b58c0" },
    { id: 32, name: "Razer BlackWidow Keyboard", price: "रु12,999", image: "https://images.unsplash.com/photo-1605902711622-cfb43c4437e6" },
    { id: 33, name: "Sony Bravia 55-inch TV", price: "रु149,999", image: "https://images.unsplash.com/photo-1606813909355-0c489fe22d9a" },
    { id: 34, name: "LG OLED TV 65-inch", price: "रु299,999", image: "https://images.unsplash.com/photo-1588776814545-7f40c63e5d4e" },
    { id: 35, name: "Philips Hue Smart Bulb", price: "रु1,999", image: "https://images.unsplash.com/photo-1612831666354-0f4e1959f6b" },
    { id: 36, name: "Samsung Galaxy Tab S8", price: "रु74,999", image: "https://images.unsplash.com/photo-1630697229227-23b1f1f3b7c6" },
    { id: 37, name: "Xiaomi Mi Band 7", price: "रु3,499", image: "https://images.unsplash.com/photo-1636967169227-23b1f1f3b7c6" },
    { id: 38, name: "Fitbit Charge 5", price: "रु12,999", image: "https://images.unsplash.com/photo-1612831666354-0f4e1959f6b" },
    { id: 39, name: "Canon PIXMA Printer", price: "रु19,999", image: "https://images.unsplash.com/photo-1600180758895-d6b1a8f7e799" },
    { id: 40, name: "Samsung Galaxy Watch 4", price: "रु29,999", image: "https://images.unsplash.com/photo-1636967169227-23b1f1f3b7c6" },
    { id: 41, name: "Xiaomi Redmi Buds 3", price: "रु2,499", image: "https://images.unsplash.com/photo-1600180758895-d6b1a8f7e798" },
    { id: 42, name: "Sony Alpha a6400", price: "रु109,999", image: "https://images.unsplash.com/photo-1606813909395-cb489fe22d9a" },
    { id: 43, name: "GoPro Hero 9", price: "रु34,999", image: "https://images.unsplash.com/photo-1624287550047-79d78008f29e" },
    { id: 44, name: "Apple Mac Mini M1", price: "रु99,999", image: "https://images.unsplash.com/photo-1517336714731-489689fd1ca8" },
    { id: 45, name: "Samsung Galaxy Book 2", price: "रु119,999", image: "https://images.unsplash.com/photo-1677184638217-9b29f27f4ec7" },
    { id: 46, name: "Apple Pencil 2", price: "रु12,999", image: "https://images.unsplash.com/photo-1612831666354-d0f4e1959f6a" },
    { id: 47, name: "Faber-Castell Sketch Pens", price: "रु3,499", image: "https://images.unsplash.com/photo-1612831666354-d0f4e1959f6a" },
    { id: 48, name: "Logitech C920 Webcam", price: "रु9,999", image: "https://images.unsplash.com/photo-1615559601203-0d2232baf47b" },
    { id: 49, name: "Sony SRS-XB43 Speaker", price: "रु12,999", image: "https://images.unsplash.com/photo-1585386959984-a415522c2f1f" },
    { id: 50, name: "Bose SoundLink Revolve", price: "रु19,999", image: "https://images.unsplash.com/photo-1585386959984-a415522c2f1f" },
    // Continue adding 51-100 similarly (mix phones, laptops, cameras, pens, shoes, smart watches, speakers, books, etc.)
];


// ---------------------- RENDER PRODUCTS ----------------------
const productGrid = document.getElementById('productGrid');
const productSearch = document.getElementById('productSearch');

function renderProducts(products) {
    productGrid.innerHTML = ""; // Clear grid before rendering
    products.forEach((prod, index) => {
        const col = document.createElement('div');
        col.className = "col-xl-3 col-lg-4 col-md-6 col-sm-12 fade-up";

        col.innerHTML = `
            <div class="card product-card shadow-sm">
                <img src="${prod.image}" class="card-img-top" alt="${prod.name}">
                <div class="card-body text-center">
                    <h5 class="card-title">${prod.name}</h5>
                    <p class="card-text price">${prod.price}</p>
                    <div class="d-flex justify-content-center gap-2 mt-2">
                        <form method="POST" action="/add-to-cart">
                            <input type="hidden" name="id" value="${prod.id}">
                            <input type="hidden" name="name" value="${prod.name}">
                            <input type="hidden" name="price" value="${prod.price}">
                            <input type="hidden" name="image" value="${prod.image}">
                            <button type="submit" class="btn btn-outline-secondary btn-sm">Add to Cart</button>
                        </form>

                        <!-- FIXED Buy Now BUTTON -->
                        <a href="/checkout/${prod.id}" class="btn btn-primary btn-sm">Buy Now</a>
                    </div>
                </div>
            </div>
        `;
        col.style.animationDelay = `${index * 0.05}s`;
        productGrid.appendChild(col);
    });
}

// INITIAL RENDER (all products)
renderProducts(allProducts);

// ---------------------- SEARCH LOGIC ----------------------
productSearch.addEventListener('input', () => {
    const query = productSearch.value.toLowerCase();
    const filteredProducts = allProducts.filter(prod => prod.name.toLowerCase().includes(query));
    renderProducts(filteredProducts);
});