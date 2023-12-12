const ProductosBtn = document.querySelector('#Productos-btn')
const ProductosUl= document.querySelector('#Productos-ul')
const ProductosBtnArrow = document.querySelector('#Productos-btn-arrow')

ProductosBtn.addEventListener('click',()=>{
    ProductosUl.style.display = (ProductosUl.style.display==='block') ?'none':'block';
    ProductosBtnArrow.style.transition= 'transform 0.3s ease'
    ProductosBtnArrow.style.transform = (ProductosBtnArrow.style.transform ==='rotate(180deg)') ? 'rotate(0deg)':'rotate(180deg)';
})

const ClienteBtn = document.querySelector('#Cliente-btn')
const ClienteUl= document.querySelector('#Cliente-ul')
const ClienteBtnArrow = document.querySelector('#Cliente-btn-arrow')

ClienteBtn.addEventListener('click',()=>{
    ClienteUl.style.display = (ClienteUl.style.display==='block') ?'none':'block';
    ClienteBtnArrow.style.transition= 'transform 0.3s ease'
    ClienteBtnArrow.style.transform = (ClienteBtnArrow.style.transform ==='rotate(180deg)') ? 'rotate(0deg)':'rotate(180deg)';
})
