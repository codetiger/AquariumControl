(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{11:function(t,e,n){t.exports=n(19)},16:function(t,e,n){},18:function(t,e,n){},19:function(t,e,n){"use strict";n.r(e);var a=n(0),o=n.n(a),c=n(3),i=n.n(c),s=(n(16),n(8)),r=n(4),l=n(5),h=n(9),u=n(6),d=n(1),m=n(10),f=n(7),p=n.n(f),v=(n(18),function(t){function e(){var t;return Object(r.a)(this,e),(t=Object(h.a)(this,Object(u.a)(e).call(this))).state={controls:{4:{name:"Tank Light",status:!0}}},t.handleChange=t.handleChange.bind(Object(d.a)(t)),t}return Object(m.a)(e,t),Object(l.a)(e,[{key:"fetchData",value:function(){var t=this;fetch("http://192.168.1.127:5000/api/controls").then((function(t){return t.json()})).then((function(e){t.setState({controls:e})})).catch((function(t){console.log(t)})),setTimeout(this.fetchData.bind(this),5e3)}},{key:"componentDidMount",value:function(){this.fetchData()}},{key:"handleChange",value:function(t,e,n){this.state.controls[n].status=t,fetch("http://192.168.1.127:5000/api/controls/"+n,{method:"PUT",headers:{Accept:"application/json","Content-Type":"application/json"},body:JSON.stringify({status:t})})}},{key:"render",value:function(){var t=this,e=this.state.controls;return console.log(e),o.a.createElement("div",{className:"example"},o.a.createElement("h2",null,"Aquarium Control"),Object.entries(e).map((function(e){var n=Object(s.a)(e,2),a=n[0],c=n[1];return o.a.createElement("div",null,o.a.createElement("label",null,o.a.createElement("span",null,c.name),o.a.createElement(p.a,{id:a,onChange:t.handleChange,checked:c.status,className:"react-switch"})))})))}}]),e}(a.Component));Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));i.a.render(o.a.createElement(v,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(t){t.unregister()}))}},[[11,1,2]]]);
//# sourceMappingURL=main.b2e370c5.chunk.js.map