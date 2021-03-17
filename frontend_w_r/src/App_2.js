import './App.css';
import React from 'react';
import {useEffect, useState} from 'react';
import SimpleSelect from './components/SimpleSelect';
import {createMuiTheme,ThemeProvider} from '@material-ui/core/styles';
import RangeSlider from './components/RangeSlider';
import Fab from '@material-ui/core/Fab';
import MultipleSelect from './components/MultipleSelect.js'
const theme = createMuiTheme({
  palette: {
    primary: {
      main:"#ea4e2f"
    }
  },
});
function App_2() {
  const api_server_url = window.location.host=="localhost:3000"?"http://127.0.0.1:8000/":(window.location.protocol+"//"+window.location.host+"/");

  const [fdata,setFdata]=useState({
    city:'',
    property_type:'',
    price:[5000,10000],
    
  })
  /**datatype: 
   * [
   * {  val:option.val,
   *    inlinetxt:option.inlineTxt
   * }
   * ]**/
  const [allcitys,setAllcitys]=useState([]);
  const [allpTypes,setAllpTypes]=useState([]);

  
  useEffect(()=>{
   
    console.log( window.location.href)
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

      const responce2=await fetch(api_server_url+"api/property/types/list/");
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
    <div>
      <div className="search_bar">

      
      <div  className="ifields">
      <ThemeProvider theme={theme}>
      <SimpleSelect key={"8285333#"} name="city" label="Citys" handelChangeFdata={handelChangeFdata} curr_value={fdata.city} op={allcitys} />
      <SimpleSelect key={"828987533#"} name="property_type" label="Property type" handelChangeFdata={handelChangeFdata} curr_value={fdata.property_type} op={allpTypes}/>

      <RangeSlider rname="price" rval={fdata.price} handelChangeFdata={handelChangeFdata}/>
      {/* <SimpleSelect key={"8k8987533#"} name="bedroom" label="Bed rooms" handelChangeFdata={handelChangeFdata} curr_value={fdata.bedroom} op={[0].map((i)=>{
        const d=[];
        for(let i=1;i<15;i++){
          d.push({val:i,inlineTxt:i});
        }
        return d;
      })[0]}/> */}
     </ThemeProvider>
      
      
      </div>
      <Fab  style={{background:"white",color:"#ea4e2f"}} onClick={()=>{
        let args="?";
        for (const key in fdata) {
         args=`${key}=${fdata[key]}&`;
        }
        window.location.assign("./property/list/"+args);
        }}>
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-search" viewBox="0 0 16 16">
      <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
      </svg>
      </Fab>
      </div>
     
      

      
     


    </div>
  );
}

export default App_2;
