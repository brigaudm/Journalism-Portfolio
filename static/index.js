document.addEventListener("DOMContentLoaded", function() {
    console.log("first event listened for");
    const buttons = document.querySelectorAll("[data-button]");
    console.log("Buttons:", buttons);

    buttons.forEach(button => {
        button.addEventListener("click", () => {
            console.log("button clicked");
            const offset = button.dataset.button === "next" ? 1 : -1;
            const articlesContainer = button.closest("[data-container]");
            const articles = articlesContainer.querySelector("[data-articles]");

            const activeArticle = articles.querySelector("[data-active]");
            let newIndex = [...articles.children].indexOf(activeArticle) + offset;
        
            if (newIndex < 0) newIndex = articles.children.length -1;
            if (newIndex >= articles.children.length) newIndex = 0;

            articles.querySelector("[data-active]").removeAttribute("data-active");
            articles.children[newIndex].setAttribute("data-active","true");
        });
    });
});