const cartGrid = document.getElementById("cartGrid");
const emptyCartMsg = document.getElementById("emptyCartMsg");

function renderCart(items) {
    cartGrid.innerHTML = "";

    if (!items || items.length === 0) {
        emptyCartMsg.style.display = "block";
        return;
    }

    emptyCartMsg.style.display = "none";

    items.forEach((item) => {
        const col = document.createElement("div");
        col.className = "col-md-4";

        col.innerHTML = `
            <div class="card h-100 shadow-sm">
                <img src="${item.image}" class="card-img-top" alt="${item.name}">
                <div class="card-body text-center">
                    <h5 class="card-title">${item.name}</h5>
                    <p class="card-text">${item.price}</p>
                </div>
            </div>
        `;
        cartGrid.appendChild(col);
    });
}

// Render on page load
renderCart(cartItems);
