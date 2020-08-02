document.querySelector('.add_announcement').addEventListener('click', (e)=>{
    ann_type = document.querySelector('#announcement_type').value
    document.querySelector('#add_ann').innerHTML = render_add_announcement(ann_type)
});


function render_add_announcement(type){
    return `
        <h3> ${type}<h3>

    <textarea width="100%" rows="4">
       
    </textarea>
    <button>Əlavə et</button>
    `;
};

document.querySelector('.edit_announcement').addEventListener('click', (e)=>{
    ann_type = document.querySelector('#announcement_select').value
    document.querySelector('#edit_ann').innerHTML = render_edit_announcement(ann_type)
});


function render_edit_announcement(type){
    return `
        <h3> ${type}<h3>
        <textarea width="100%" rows="4">Redaktə olunacaq elan</textarea>
        
        <button>Redaktə et</button>`;
};