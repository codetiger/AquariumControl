(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{38:function(t,e,n){t.exports=n(51)},43:function(t,e,n){},44:function(t,e,n){},51:function(t,e,n){"use strict";n.r(e);var a=n(0),o=n.n(a),c=n(11),r=n.n(c),i=(n(43),n(33)),l=n(27),s=n(14),h=n(28),u=n(29),m=n(9),d=n(34),p=n(84),f=n(86),w=n(78),v=n(21),E=n(79),g=n(87),b=n(81),y=n(82),j=n(80),k=n(85),O=n(31),C=n.n(O),D=n(77),T=n(32),J=n(76),P=(n(44),Object(T.a)({palette:{primary:J.a}})),x=function(t){function e(){var t;return Object(l.a)(this,e),(t=Object(h.a)(this,Object(u.a)(e).call(this))).handleChange=function(e){return function(n){var a=t.state.controls;e in a&&(a[e].status=n.target.checked);var o=window.location.protocol+"//"+window.location.hostname+(window.location.port?":"+window.location.port:"");fetch(o+"/api/controls/"+e,{method:"PUT",headers:{Accept:"application/json","Content-Type":"application/json"},body:JSON.stringify({status:n.target.checked})})}},t.state={controls:{4:{name:"Tank Light",status:!0},6:{name:"Plant Light",status:!1}}},t.handleChange=t.handleChange.bind(Object(m.a)(t)),t}return Object(d.a)(e,t),Object(s.a)(e,[{key:"fetchData",value:function(){var t=this,e=window.location.protocol+"//"+window.location.hostname+(window.location.port?":"+window.location.port:"");fetch(e+"/api/controls").then((function(t){return t.json()})).then((function(e){t.setState({controls:e})})).catch((function(t){console.log(t)})),setTimeout(this.fetchData.bind(this),5e3)}},{key:"componentDidMount",value:function(){this.fetchData()}},{key:"render",value:function(){var t=this,e=this.state.controls;return o.a.createElement(D.a,{theme:P},o.a.createElement("div",{className:"example"},o.a.createElement(f.a,{position:"static",color:"primary"},o.a.createElement(w.a,null,o.a.createElement(v.a,{variant:"h6"},"Aquarium Control Panel"))),Object.entries(e).map((function(e){var n=Object(i.a)(e,2),a=n[0],c=n[1];return o.a.createElement("div",null,o.a.createElement(E.a,null,o.a.createElement(g.a,null,o.a.createElement(j.a,null,o.a.createElement(k.a,null,o.a.createElement(C.a,{color:"primary"}))),o.a.createElement(b.a,{primary:c.name,secondary:c.name}),o.a.createElement(p.a,{id:a,onChange:t.handleChange(a),checked:c.status,color:"primary"})),o.a.createElement(y.a,null)))}))))}}]),e}(a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));r.a.render(o.a.createElement(x,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(t){t.unregister()}))}},[[38,1,2]]]);
//# sourceMappingURL=main.65251d4a.chunk.js.map