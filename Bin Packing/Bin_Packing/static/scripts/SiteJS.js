$(document).ready(function () {
    if ($("#alg").val() === 'First Fit') {
        $("#Radio1").prop("checked", true);

    } else if ($("#alg").val() === 'First Fit Decreasing') {
        $("#Radio2").prop("checked", true);
    } else if ($("#alg").val() === 'Best Fit') {
        $("#Radio3").prop("checked", true);
    }
});

function checkInput(ob) {
    var invalidChars = /[^0-9 ]/;
    if (invalidChars.test(ob.value)) {
        ob.value = ob.value.replace(invalidChars, "");
    }
}