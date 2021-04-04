function addRecipe(e) {
    // e.preventDefault()
    result = document.getElementById('result')

    recipeName = document.getElementById('recipeName').value
    recipeDescription = document.getElementById('recipeDescription').value
    prepTime = document.getElementById('prepTime').value
    preparation = document.getElementById('preparation').value
    ingredients = document.getElementById('ingredients').value

    if (recipeName == '') {
        result.innerText = 'Uzupelnij nazwe przepisu'
    } else if (recipeDescription == '') {
        result.innerText = 'Uzupelnij Opis'
    } else if (prepTime == '') {
        result.innerText = 'Uzupelnij Czas Przygotowania'
    } else if (preparation == '') {
        result.innerText = 'Uzupelnij Opis Przygotowania'
    } else if (ingredients == '') {
        result.innerText = 'Uzupelnij Skladniki'
    } else {
        $.ajax({

            url: '/recipe/add/',
            type: 'POST',
            data: {
                // headers: { 'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')},
                recipeName: recipeName,
                recipeDescription: recipeDescription,
                prepTime: prepTime,
                preparation: preparation,
                ingredients: ingredients,
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
            }
        }).done(function () {
            window.location.replace("/recipe/list");
        })
    }
}