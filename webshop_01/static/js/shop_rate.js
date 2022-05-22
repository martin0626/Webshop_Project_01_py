function addStars() {
            let ratingList = Array.from(document.getElementsByClassName('rating'));
            ratingList.forEach(addElements);

            function addElements(item) {
                let starsYellow = Number(item.getAttribute("data-rating"));
                let whiteStars = 5 - starsYellow;
                let htmlStr = '';
                for (let i = 0; i < starsYellow; i++) {
                    htmlStr += `<i class="text-warning fa fa-star"></i>\n`
                }
                for (let i = 0; i < whiteStars; i++) {
                    htmlStr += `<i class="text-muted fa fa-star"></i>\n`
                }
                item.innerHTML = htmlStr
            }
        }
        addStars();