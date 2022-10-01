/* eslint-disable */

import { useParams } from "react-router-dom";

  function DetailCard(props){

    let {id} = useParams(); //app.js에서 detail/:id 로 정의했는데 여기 들어가는 id를 저장함
    
    let found = props.shoes.find(function(x){
      return x.id == id;
    })

    return (
      <div className="container">

        <div className="row">
          <div className="col-md-6">
            <img src={"https://codingapple1.github.io/shop/shoes"+(parseInt(found.id)+1)+".jpg"} width="100%" />
          </div>
          <div className="col-md-6">
            <h4 className="pt-5">{found.title}</h4>
            <p>{found.content}</p>
            <p>{found.price}</p>
            <button className="btn btn-danger">주문하기</button> 
          </div>
        </div>
      </div> 
    )
  }


export default DetailCard;