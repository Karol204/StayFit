function addRecipe(e) {
    // e.preventDefault()
    let result = document.getElementById('result')

    let recipeName = document.getElementById('recipeName').value
    let recipeDescription = document.getElementById('recipeDescription').value
    let prepTime = document.getElementById('prepTime').value
    let preparation = document.getElementById('preparation').value
    let ingredients = document.getElementById('ingredients').value

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
                recipeName: recipeName,
                recipeDescription: recipeDescription,
                prepTime: prepTime,
                preparation: preparation,
                ingredients: ingredients,
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
            }
        }).done(function () {
            window.location.replace("/recipe/list");
        }).fail(function (response){
            result.innerText = response['errorMessage']
        })
    }
}

function addPlan() {
    let planName = document.getElementById('planName').value
    let planDescription = document.getElementById('planDescription').value

    let result = document.querySelector('.result')
    if (planName == ''){
        result.innerText = 'Uzupelnij Nazwe planu'
    } else if (planDescription == ''){
        result.innerText = 'Uzupelnij Opis planu'
    } else{
        $.ajax({
            url: '/plan/add/',
            type: 'POST',
            data: {
                planName: planName,
                planDescription: planDescription,
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
            }
        }).done(function (response) {
            result.innerText = response['errorMessage']
        }).fail(function (response){
            console.log('gsdgdfd')
            result.innerText = response['errorMessage']
        })
    }
}