<%inherit file="html5-doc.tmpl"/>
<%block name="body">
<%include file="yandex-metrika.tmpl"/>
<%include file="core.tmpl"/>
<%include file="secondline.tmpl"/>
</%block>
<%block name="output">
<%
    import markdown
    import codecs

    html = markdown.markdown( codecs.open( "../bible.md", "r", "utf-8" ).read() )    
%>
<div class = "left100" style = "width: 600px;">
${html}
</div>
</%block>