let alertWrapper = document.querySelector('.alert');
let alertClose = document.querySelector('.alert__close');

//if (alertWrapper) {
//  alertClose.addEventListener('click', () =>
//    alertWrapper.style.display = 'none'
//)}

alertClose.forEach(function (item) {
    item.addEventListener('click', function () {
        parentModal = this.closest('.alert');
        parentModal.style.display = 'none';
    });
});
