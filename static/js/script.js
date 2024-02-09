// الحصول على زر فتح الصفحة المنبثقة
var openPopupBtn = document.getElementById("openPopup");

// الحصول على زر إغلاق الصفحة المنبثقة
var closePopupBtn = document.getElementById("closePopup");

// الحصول على الصفحة المنبثقة
var popup = document.getElementById("popup");

// عند النقر على زر فتح الصفحة المنبثقة
openPopupBtn.onclick = function() {
    popup.style.display = "block"; // إظهار الصفحة المنبثقة
}

// عند النقر على زر إغلاق الصفحة المنبثقة
closePopupBtn.onclick = function() {
    popup.style.display = "none"; // إخفاء الصفحة المنبثقة
}

// عند النقر خارج الصفحة المنبثقة (على الخلفية)
window.onclick = function(event) {
    if (event.target == popup) {
        popup.style.display = "none"; // إخفاء الصفحة المنبثقة
    }
}
