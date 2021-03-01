import CssBaseline from '@material-ui/core/CssBaseline';
import './App.css';
import {useEffect, useState} from 'react';
import Container from '@material-ui/core/Container';
import SimpleSelect from './components/SimpleSelect';
import RangeSlider from './components/RangeSlider';
function App() {
  const api_server_url="http://127.0.0.1:8000/";
  const [fdata,setFdata]=useState({
    city:'',
    property_type:'',
    price:[5000,10000],
  })
  //[{val:option.val,inlinetxt:option.inlineTxt}]
  const [allcitys,setAllcitys]=useState([]);
  const [allpTypes,setAllpTypes]=useState([]);

  
  useEffect(()=>{
    async function fetchdata(){
      const responce=await fetch(api_server_url+"api/city/");
      const data=await responce.json();
      // console.log(data);
      data.forEach(element => {
        // element.name

        //  console.log([...allcitys]);
        allcitys.push({val:element.name,inlineTxt:element.name});
       
        setAllcitys([...allcitys]);
      });

      const responce2=await fetch(api_server_url+"api/propertytype/list/");
      const data2=await responce2.json();
      // console.log(data);
      data2.forEach(element => {
        // element.name

        //  console.log([...allcitys]);
        allpTypes.push({val:element.id,inlineTxt:element.name});
       
        setAllpTypes([...allpTypes]);
      });

    }
    fetchdata();
  },[])

  function handelChangeFdata(event){
    // event.terget.name
    console.log(event.target.name);
    setFdata({...fdata,[event.target.name]:event.target.value});
  }
  return (
    <CssBaseline>
    <Container >
      <div  className="ifields">
      <SimpleSelect name="city" label="Citys" handelChangeFdata={handelChangeFdata} curr_value={fdata.city} op={allcitys} />
      <SimpleSelect name="property_type" label="Property type" handelChangeFdata={handelChangeFdata} curr_value={fdata.property_type} op={allpTypes}/>

      <RangeSlider rname="price" rval={fdata.price} handelChangeFdata={handelChangeFdata}/>
      </div>

      
     

    </Container>
    </CssBaseline>
  );
}

export default App;
