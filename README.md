<p>pip install uvicorn</p>
<p>pip install fastapi</p>

<p>uvicorn main:app --reload</p>


<table> 
    <tr>
        <th>url</th>
        <th>method</th>
        <th>action</th>
    </tr>
    <tr>
        <td>/</td>
        <td>get</td>
        <td>list data</td>
    </tr>
    <tr>
        <td>/</td>
        <td>post</td>
        <td>Create Data: data = {name_product: str, price: int}</td>
    </tr>
    <tr>
        <td>/id</td>
        <td>get</td>
        <td>detail</td>
    </tr>
    <tr>
        <td>/id</td>
        <td>delete</td>
        <td>delete data</td>
    </tr>
    <tr>
        <td>/id</td>
        <td>put</td>
        <td>Create Data: data = {name_product: str, price: int}</td>
    </tr>

</table>