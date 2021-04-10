    let likeBtnContainer = document.getElementById('likeBtnContainer')


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

function addRecipeToPlan() {
    let result = document.querySelector('.result')


    let chosenPlan = document.getElementById('id_plan').value
    let chosenMeal = document.getElementById('id_meal_name').value
    let mealNumber = document.getElementById('id_order').value
    let recipe = document.getElementById('id_recipe').value
    let dayName = document.getElementById('id_day_name').value
    if (chosenPlan == ''){
        result.innerText = 'Wybierz plan do ktorego chcesz dodac przepis'
    } else if (chosenMeal == ''){
        result.innerText = 'Wybierz posilek'
    } else if (mealNumber == ''){
        result.innerText = 'Wybierz numer posilku w dniu'
    } else if (recipe == ''){
        result.innerText = 'Wybierz przepis ktory chcesz dodac jako posilek'
    } else if (dayName == ''){
        result.innerText = 'Wybierz dzien do ktorego chcesz przypisac posilek'
    } else {
        $.ajax({
            url: '/plan/add-recipe/',
            type: 'POST',
            data: {
                chosenPlan: chosenPlan,
                chosenMeal: chosenMeal,
                mealNumber: mealNumber,
                recipe: recipe,
                dayName:dayName,
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
            }
        }).done(function (response) {
            result.innerText = response['errorMessage']
        }).fail(function (response){
            result.innerText = response['errorMessage']
        })
    }
}

function likeRecipe() {
    let url = window.location.href
    let arr = url.split('/')
    let id = arr[arr.length - 1]
    let recipeId = parseInt(id)
    $.ajax({
         url: '/plan/like/',
            type: 'POST',
            data: {
                recipeId:recipeId,
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
            }
    }).done(function (response){
        localStorage.setItem('liked' + recipeId, 'liked')
        checkBtn(recipeId)
    })
}

function dislikeRecipe() {
    let url = window.location.href
    let arr = url.split('/')
    let id = arr[arr.length - 1]
    let recipeId = parseInt(id)
    $.ajax({
         url: '/plan/dislike/',
            type: 'POST',
            data: {
                recipeId:recipeId,
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
            }
    }).done(function (response){
        localStorage.clear()
        checkBtn()
    })
}


function checkBtn() {
    let url = window.location.href
    let arr = url.split('/')
    let id = arr[arr.length - 1]
    let recipeId = parseInt(id)
    let storage = localStorage.getItem('liked' + recipeId)
    console.log(storage)
    if (storage == 'liked'){
        likeBtnContainer.innerHTML
            = '<button className="btn btn-color rounded-0 pt-0 pb-0 pr-4 pl-4" id="dislikeBtn" onClick="dislikeRecipe()" data-id="{{ recipe.id }}">Nie lub</button>'
    }
}

checkBtn()