const scriptURL="",form=document.forms["application-form"];let res;function successs(){$("#success").removeClass("d-none"),$("#wait").addClass("d-none"),200!==res.status&&($("#success").addClass("d-none"),$("#fail").removeClass("d-none"))}form.addEventListener("submit",t=>{t.preventDefault(),$("#submit-btn").addClass("d-none"),document.getElementById("wait").classList.remove("d-none"),fetch("",{method:"POST",body:new FormData(form)}).then(t=>{res=t,console.log("Success!",t)}).catch(t=>{console.error("Error!",t.message),$("#fail").removeClass("d-none"),$("#success").addClass("d-none")}),setTimeout(successs,5e3)});var apikey="";function readURL(t){if(t.files&&t.files[0]){var e=new FileReader;e.onload=function(t){$("#imageResult").attr("src",t.target.result)},e.readAsDataURL(t.files[0])}}$((function(){$("#upload").on("change",(function(){readURL(input),uploadimage("upload")}))}));var input=document.getElementById("upload"),infoArea=document.getElementById("upload-label"),urllink=document.getElementById("urllink");function showFileName(t){var e=t.srcElement.files[0].name;infoArea.textContent="File name: "+e}function uploadimage(t){var e=document.getElementById(t),n=new FormData;n.append("image",e.files[0]);var i={url:"https://api.imgbb.com/1/upload?key="+apikey,method:"POST",timeout:0,processData:!1,mimeType:"multipart/form-data",contentType:!1,data:n};$.ajax(i).done((function(t){console.log(t);var e=JSON.parse(t);console.log(e.data.url),urllink.innerHTML=e.data.url}))}input.addEventListener("change",showFileName),$(document).on("dragstart dragenter dragover",(function(t){$("#image-drag-drop").removeClass("d-none"),dropZoneVisible=!0})).on("drop dragleave dragend",(function(t){dropZoneTimer=setTimeout((function(){dropZoneVisible||$("#image-drag-drop").addClass("d-none")}),50),clearTimeout(dropZoneTimer)})),function(t){"use strict";function e(e,n){this.itemsArray=[],this.$element=t(e),this.$element.hide(),this.isSelect="SELECT"===e.tagName,this.multiple=this.isSelect&&e.hasAttribute("multiple"),this.objectItems=n&&n.itemValue,this.placeholderText=e.hasAttribute("placeholder")?this.$element.attr("placeholder"):"",this.inputSize=Math.max(1,this.placeholderText.length),this.$container=t('<div class="bootstrap-tagsinput"></div>'),this.$input=t('<input type="text" placeholder="'+this.placeholderText+'"/>').appendTo(this.$container),this.$element.before(this.$container),this.build(n)}function n(t,e){if("function"!=typeof t[e]){var n=t[e];t[e]=function(t){return t[n]}}}function i(t,e){if("function"!=typeof t[e]){var n=t[e];t[e]=function(){return n}}}function a(t){return t?s.text(t).html():""}function o(t){var e=0;if(document.selection){t.focus();var n=document.selection.createRange();n.moveStart("character",-t.value.length),e=n.text.length}else(t.selectionStart||"0"==t.selectionStart)&&(e=t.selectionStart);return e}var r={tagClass:function(t){return"label label-info"},itemValue:function(t){return t?t.toString():t},itemText:function(t){return this.itemValue(t)},itemTitle:function(t){return null},freeInput:!0,addOnBlur:!0,maxTags:void 0,maxChars:void 0,confirmKeys:[13,44],delimiter:",",delimiterRegex:null,cancelConfirmKeysOnEmpty:!0,onTagExists:function(t,e){e.hide().fadeIn()},trimValue:!1,allowDuplicates:!1};e.prototype={constructor:e,add:function(e,n,i){var o=this;if(!(o.options.maxTags&&o.itemsArray.length>=o.options.maxTags)&&(!1===e||e)){if("string"==typeof e&&o.options.trimValue&&(e=t.trim(e)),"object"==typeof e&&!o.objectItems)throw"Can't add objects when itemValue option is not set";if(!e.toString().match(/^\s*$/)){if(o.isSelect&&!o.multiple&&o.itemsArray.length>0&&o.remove(o.itemsArray[0]),"string"==typeof e&&"INPUT"===this.$element[0].tagName){var r=o.options.delimiterRegex?o.options.delimiterRegex:o.options.delimiter,s=e.split(r);if(s.length>1){for(var l=0;l<s.length;l++)this.add(s[l],!0);return void(n||o.pushVal())}}var u=o.options.itemValue(e),c=o.options.itemText(e),p=o.options.tagClass(e),m=o.options.itemTitle(e),d=t.grep(o.itemsArray,(function(t){return o.options.itemValue(t)===u}))[0];if(!d||o.options.allowDuplicates){if(!(o.items().toString().length+e.length+1>o.options.maxInputLength)){var h=t.Event("beforeItemAdd",{item:e,cancel:!1,options:i});if(o.$element.trigger(h),!h.cancel){o.itemsArray.push(e);var f=t('<span class="tag '+a(p)+(null!==m?'" title="'+m:"")+'">'+a(c)+'<span data-role="remove"></span></span>');if(f.data("item",e),o.findInputWrapper().before(f),f.after(" "),o.isSelect&&!t('option[value="'+encodeURIComponent(u)+'"]',o.$element)[0]){var g=t("<option selected>"+a(c)+"</option>");g.data("item",e),g.attr("value",u),o.$element.append(g)}n||o.pushVal(),(o.options.maxTags===o.itemsArray.length||o.items().toString().length===o.options.maxInputLength)&&o.$container.addClass("bootstrap-tagsinput-max"),o.$element.trigger(t.Event("itemAdded",{item:e,options:i}))}}}else if(o.options.onTagExists){var v=t(".tag",o.$container).filter((function(){return t(this).data("item")===d}));o.options.onTagExists(e,v)}}}},remove:function(e,n,i){var a=this;if(a.objectItems&&(e=(e="object"==typeof e?t.grep(a.itemsArray,(function(t){return a.options.itemValue(t)==a.options.itemValue(e)})):t.grep(a.itemsArray,(function(t){return a.options.itemValue(t)==e})))[e.length-1]),e){var o=t.Event("beforeItemRemove",{item:e,cancel:!1,options:i});if(a.$element.trigger(o),o.cancel)return;t(".tag",a.$container).filter((function(){return t(this).data("item")===e})).remove(),t("option",a.$element).filter((function(){return t(this).data("item")===e})).remove(),-1!==t.inArray(e,a.itemsArray)&&a.itemsArray.splice(t.inArray(e,a.itemsArray),1)}n||a.pushVal(),a.options.maxTags>a.itemsArray.length&&a.$container.removeClass("bootstrap-tagsinput-max"),a.$element.trigger(t.Event("itemRemoved",{item:e,options:i}))},removeAll:function(){var e=this;for(t(".tag",e.$container).remove(),t("option",e.$element).remove();e.itemsArray.length>0;)e.itemsArray.pop();e.pushVal()},refresh:function(){var e=this;t(".tag",e.$container).each((function(){var n=t(this),i=n.data("item"),o=e.options.itemValue(i),r=e.options.itemText(i),s=e.options.tagClass(i);(n.attr("class",null),n.addClass("tag "+a(s)),n.contents().filter((function(){return 3==this.nodeType}))[0].nodeValue=a(r),e.isSelect)&&t("option",e.$element).filter((function(){return t(this).data("item")===i})).attr("value",o)}))},items:function(){return this.itemsArray},pushVal:function(){var e=this,n=t.map(e.items(),(function(t){return e.options.itemValue(t).toString()}));e.$element.val(n,!0).trigger("change")},build:function(e){var a=this;if(a.options=t.extend({},r,e),a.objectItems&&(a.options.freeInput=!1),n(a.options,"itemValue"),n(a.options,"itemText"),i(a.options,"tagClass"),a.options.typeahead){var s=a.options.typeahead||{};i(s,"source"),a.$input.typeahead(t.extend({},s,{source:function(e,n){function i(t){for(var e=[],i=0;i<t.length;i++){var r=a.options.itemText(t[i]);o[r]=t[i],e.push(r)}n(e)}this.map={};var o=this.map,r=s.source(e);t.isFunction(r.success)?r.success(i):t.isFunction(r.then)?r.then(i):t.when(r).then(i)},updater:function(t){return a.add(this.map[t]),this.map[t]},matcher:function(t){return-1!==t.toLowerCase().indexOf(this.query.trim().toLowerCase())},sorter:function(t){return t.sort()},highlighter:function(t){var e=new RegExp("("+this.query+")","gi");return t.replace(e,"<strong>$1</strong>")}}))}if(a.options.typeaheadjs){var l=null,u={},c=a.options.typeaheadjs;t.isArray(c)?(l=c[0],u=c[1]):u=c,a.$input.typeahead(l,u).on("typeahead:selected",t.proxy((function(t,e){u.valueKey?a.add(e[u.valueKey]):a.add(e),a.$input.typeahead("val","")}),a))}a.$container.on("click",t.proxy((function(t){a.$element.attr("disabled")||a.$input.removeAttr("disabled"),a.$input.focus()}),a)),a.options.addOnBlur&&a.options.freeInput&&a.$input.on("focusout",t.proxy((function(e){0===t(".typeahead, .twitter-typeahead",a.$container).length&&(a.add(a.$input.val()),a.$input.val(""))}),a)),a.$container.on("keydown","input",t.proxy((function(e){var n=t(e.target),i=a.findInputWrapper();if(a.$element.attr("disabled"))a.$input.attr("disabled","disabled");else{switch(e.which){case 8:if(0===o(n[0])){var r=i.prev();r.length&&a.remove(r.data("item"))}break;case 46:if(0===o(n[0])){var s=i.next();s.length&&a.remove(s.data("item"))}break;case 37:var l=i.prev();0===n.val().length&&l[0]&&(l.before(i),n.focus());break;case 39:var u=i.next();0===n.val().length&&u[0]&&(u.after(i),n.focus())}var c=n.val().length;Math.ceil(c/5),n.attr("size",Math.max(this.inputSize,n.val().length))}}),a)),a.$container.on("keypress","input",t.proxy((function(e){var n=t(e.target);if(a.$element.attr("disabled"))a.$input.attr("disabled","disabled");else{var i=n.val(),o=a.options.maxChars&&i.length>=a.options.maxChars;a.options.freeInput&&(function(e,n){var i=!1;return t.each(n,(function(t,n){if("number"==typeof n&&e.which===n)return i=!0,!1;if(e.which===n.which){var a=!n.hasOwnProperty("altKey")||e.altKey===n.altKey,o=!n.hasOwnProperty("shiftKey")||e.shiftKey===n.shiftKey,r=!n.hasOwnProperty("ctrlKey")||e.ctrlKey===n.ctrlKey;if(a&&o&&r)return i=!0,!1}})),i}(e,a.options.confirmKeys)||o)&&(0!==i.length&&(a.add(o?i.substr(0,a.options.maxChars):i),n.val("")),!1===a.options.cancelConfirmKeysOnEmpty&&e.preventDefault());var r=n.val().length;Math.ceil(r/5),n.attr("size",Math.max(this.inputSize,n.val().length))}}),a)),a.$container.on("click","[data-role=remove]",t.proxy((function(e){a.$element.attr("disabled")||a.remove(t(e.target).closest(".tag").data("item"))}),a)),a.options.itemValue===r.itemValue&&("INPUT"===a.$element[0].tagName?a.add(a.$element.val()):t("option",a.$element).each((function(){a.add(t(this).attr("value"),!0)})))},destroy:function(){var t=this;t.$container.off("keypress","input"),t.$container.off("click","[role=remove]"),t.$container.remove(),t.$element.removeData("tagsinput"),t.$element.show()},focus:function(){this.$input.focus()},input:function(){return this.$input},findInputWrapper:function(){for(var e=this.$input[0],n=this.$container[0];e&&e.parentNode!==n;)e=e.parentNode;return t(e)}},t.fn.tagsinput=function(n,i,a){var o=[];return this.each((function(){var r=t(this).data("tagsinput");if(r)if(n||i){if(void 0!==r[n]){if(3===r[n].length&&void 0!==a)var s=r[n](i,null,a);else s=r[n](i);void 0!==s&&o.push(s)}}else o.push(r);else r=new e(this,n),t(this).data("tagsinput",r),o.push(r),"SELECT"===this.tagName&&t("option",t(this)).attr("selected","selected"),t(this).val(t(this).val())})),"string"==typeof n?o.length>1?o:o[0]:o},t.fn.tagsinput.Constructor=e;var s=t("<div />");t((function(){t("input[data-role=tagsinput], select[multiple][data-role=tagsinput]").tagsinput()}))}(window.jQuery),$(document).ready((function(){$('input[data-role="tagsinput"]').each((function(t,e){var n=e.dataset.class;n&&$(e).tagsinput({tagClass:function(){return"label "+n}})}))}));