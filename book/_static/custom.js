function is_in_preffix_list(s, preffix_list) {
    for (let preffix of preffix_list) {
        if(s.startsWith(preffix)) {
            return true;
        }
    }
    return false;
}

function basename (path) {
    return path.substring(path.lastIndexOf('/') + 1)
}

function add_ticks() {
    const html_code_tick_vert = 
    '<svg role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z" fill="#28a745" stroke="#28a745"></path></svg>';
    '<svg role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z" fill="#28a745" stroke="#28a745"></path></svg>'
    const html_code_tick_orange = html_code_tick_vert.replace("#28a745", "#f0b37e").replace("#28a745", "#f0b37e");

    let list_passed = Array();
    let list_en_cours = Array();
    for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if(key.startsWith("Pythonpad-save-files-")) {
            const preffix_len = "Pythonpad-save-files-".length;
            d_files = JSON.parse(localStorage.getItem(key));
            if(".passed.json" in d_files) {
                list_passed.push(key.slice(preffix_len).replaceAll(".", "_"));
            }
        } else if (key.startsWith("Pythonpad-save-src-")) {
            const preffix_len = "Pythonpad-save-src-".length;
            if(!list_passed.includes(key.slice(preffix_len).replaceAll(".", "_"))) {
                list_en_cours.push(key.slice(preffix_len).replaceAll(".", "_"));
            }
        }
    }

    var elements = document.getElementsByClassName("reference internal");
    for (let item of elements) {
        let href_attribute = item.getAttribute("href");
        if (href_attribute == "#") {
            href_attribute = basename(window.location.href);
        }
        let innerHTML = item.innerHTML.replace(html_code_tick_vert, "").replace(html_code_tick_orange, "");
        if(is_in_preffix_list(href_attribute, list_passed)) {
            item.innerHTML = innerHTML + ' ' + html_code_tick_vert;
        } else if(is_in_preffix_list(href_attribute, list_en_cours)) {
            item.innerHTML = innerHTML + ' ' + html_code_tick_orange;
        } else {
            item.innerHTML = innerHTML;
        }
    }
}

document.addEventListener("DOMContentLoaded", add_ticks);

el = document.querySelectorAll("#pad button");
for (let i = 0; i < el.length; i++) {
    el[i].addEventListener("click", add_ticks);
}
