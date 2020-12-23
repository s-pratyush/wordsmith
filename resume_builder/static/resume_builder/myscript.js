var checker = document.getElementById("checkbox");
var sendbtn = document.getElementById("submit_btn");
// when unchecked or checked, run the function
checker.onchange = function () {
    if (this.checked) {
        sendbtn.disabled = false;
    } else {
        sendbtn.disabled = true;
    }
    var skills = document.getElementsByClassName('tag')
    var skillset = ""
    for (var skill of skills) {
        skill = skill.innerHTML.split("<")[0]
        skillset = skillset + "," + skill
    }
    document.getElementById('tag-input1').value = skillset
    console.log(document.getElementById('tag-input1').value)
};

