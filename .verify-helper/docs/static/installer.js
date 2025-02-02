const data = {};
data["verify.yml"] = (function () {
    const req = new XMLHttpRequest();
    req.open("GET", "https://raw.githubusercontent.com/kzrnm/verification-helper/master/.github/workflows/verify.yml", false);
    req.send();
    return req.responseText;
})();
data["example.test.cpp"] = (function () {
    const req = new XMLHttpRequest();
    req.open("GET", "https://raw.githubusercontent.com/kzrnm/verification-helper/master/example.test.cpp", false);
    req.send();
    return req.responseText;
})();

const input = document.getElementById("input");
const inputBranch = document.getElementById("input-branch");
const output = document.getElementById("output");
const output2 = document.getElementById("output2");
const output3 = document.getElementById("output3");
const output4 = document.getElementById("output4");
const output5 = document.getElementById("output5");
const output6 = document.getElementById("output6");
const output7 = document.getElementById("output7");
const output8 = document.getElementById("output8");
const output9 = document.getElementById("output9");
const output10 = document.getElementById("output10");
const output11 = document.getElementById("output11");
const output12 = document.getElementById("output12");
const output13 = document.getElementById("output13");

function retrieveDefaultBranch() {
    const found = input.value.match(/\/github.com\/([^\/]+)\/([^\/]+)/);
    if (!found) return;
    const url = "https://api.github.com/repos/" + found[1] + "/" + found[2];
    const req = new XMLHttpRequest();
    req.open("GET", url, false);
    req.send();
    const resp = JSON.parse(req.responseText);
    if (resp['default_branch']) {
        inputBranch.value = resp['default_branch'];
    }
}

function updateLinks() {
    const found = input.value.match(/\/github.com\/([^\/]+)\/([^\/]+)/);
    if (found) {
        const url = input.value.replace(/\/$/, "");
        const ghpages = "https://" + found[1] + ".github.io/" + found[2] + "/";
        const branch = inputBranch.value;

        // adding verify.yml
        const filename = ".github%2Fworkflows%2Fverify.yml"
        const value = encodeURIComponent(data["verify.yml"].replace("git+https://github.com/kzrnm/verification-helper.git@master", "online-judge-verify-helper"));
        output.href = url + "/new/" + branch + "?filename=" + filename + "&value=" + value;
        output.textContent = url + "&value=...";

        // adding example.text.cpp
        const filename2 = "example.test.cpp";
        const value2 = encodeURIComponent(data["example.test.cpp"]);
        output2.href = url + "/new/" + branch + "?filename=" + filename2 + "&value=" + value2;

        // links to GitHub Actions
        output3.href = input.value.replace(/\/$/, "") + "/actions";
        output5.href = input.value.replace(/\/$/, "") + "/actions";

        // badges of GitHub Actions
        output4.textContent = "[![Actions Status](" + url + "/workflows/verify/badge.svg)](" + url + "/actions)";
        output6.src = url + "/workflows/verify/badge.svg";
        output7.src = url + "/workflows/verify/badge.svg";

        // links to GitHub Pages
        output8.href = ghpages;
        output11.href = ghpages;

        // badges of GitHub Pages
        output10.textContent = "[![GitHub Pages](https://img.shields.io/static/v1?label=GitHub+Pages&message=+&color=brightgreen&logo=github)](" + ghpages + ")";
        output9.src = "https://img.shields.io/static/v1?label=GitHub+Pages&message=+&color=brightgreen&logo=github";
        output12.src = "https://img.shields.io/static/v1?label=GitHub+Pages&message=+&color=brightgreen&logo=github";

        // links to gh-pages branch
        output13.href = url + "/commits/gh-pages";
    }
}

function update() {
    retrieveDefaultBranch();
    updateLinks();
}

input.addEventListener('change', update);
input.addEventListener('keyup', update);
inputBranch.addEventListener('change', updateLinks);
inputBranch.addEventListener('keyup', updateLinks);
updateLinks();
