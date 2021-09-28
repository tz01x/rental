import "./App.css";
import React from "react";

import { useEffect, useState } from "react";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import { createTheme, ThemeProvider } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import ButtonGroup from "@material-ui/core/ButtonGroup";
import { Fade } from "@material-ui/core/";
import ToggleButton from "@material-ui/lab/ToggleButton";
import ToggleButtonGroup from "@material-ui/lab/ToggleButtonGroup";

import SimpleSelect from "./components/SimpleSelect";
import RangeSlider from "./components/RangeSlider";
import MultipleSelect from "./components/MultipleSelect.js";
const theme = createTheme({
  palette: {
    primary: {
      main: "#ea4e2f"
    }
  }
});
function App() {
  const ak = "";
  const api_server_url =
    window.location.host == "localhost:3000"
      ? "http://127.0.0.1:8000/"
      : window.location.protocol + "//" + window.location.host + "/";

  console.log(api_server_url);
  const [fdata, setFdata] = useState({
    city: "",
    property_type: "",
    price: [5000, 100000],
    bedroom: "",
    bathroom: "",
    features: []
  });
  /**datatype:
   * [
   * {  val:option.val,
   *    inlinetxt:option.inlineTxt
   * }
   * ]**/
  const [allcitys, setAllcitys] = useState([]);
  const [allpTypes, setAllpTypes] = useState([]);
  const [allfeatures, setAllfeatures] = useState([]);
  const [myproperty, setMyProperty] = useState([]);

  function savetoStroage(name, data) {
    sessionStorage.setItem(name, JSON.stringify(data));
  }
  function getformStroage(name) {
    return sessionStorage.getItem(name)
      ? JSON.parse(sessionStorage.getItem(name))
      : null;
  }
  function stroage_is_Exit(name) {
    return sessionStorage.getItem(name) ? true : false;
  }
  async function load_fatch_Data(
    storage_key,
    url,
    state,
    setState,
    f,
    featch_from_api = false,
    get_raw_data = false
  ) {
    ///state is what you want to save affter featching all iterating over all the data
    ///f is a callback funcitn is for each responce data ..
    let fetch_api = false;
    if (stroage_is_Exit(storage_key) && !featch_from_api) {
      setState(getformStroage(storage_key));
    } else {
      fetch_api = true;
    }
    if (featch_from_api || fetch_api) {
      const responce = await fetch(api_server_url + url);
      let data = await responce.json();
      // console.log(data);
      if (get_raw_data) {
        f(data);
      } else {
        if (data.hasOwnProperty("results")) {
          data = data.results;
        }
        data.forEach((element) => {
          // element.name

          //  console.log([...allcitys]);
          // state.push({ val: element.name, inlineTxt: element.name });

          // setState([...state]);

          f(element);
        });
        savetoStroage(storage_key, state);
      }
    }
  }

  useEffect(() => {
    // sessionStorage.clear();

    async function fetchdata() {
      await load_fatch_Data(
        "citys",
        "api/city/",
        allcitys,
        setAllcitys,
        (element) => {
          allcitys.push({ val: element.name, inlineTxt: element.name });
          setAllcitys([...allcitys]);
        }
      );
      await load_fatch_Data(
        "ptyps",
        "api/property/types/list/",
        allpTypes,
        setAllpTypes,
        (element) => {
          allpTypes.push({ val: element.name, inlineTxt: element.name });
          setAllpTypes([...allpTypes]);
        }
      );

      await load_fatch_Data(
        "features",
        "api/property/features/list/",
        allfeatures,
        setAllfeatures,
        (element) => {
          allfeatures.push(element.name);
          setAllfeatures([...allfeatures]);
        }
      );

      await load_fatch_Data(
        "propertylist",
        "api/property/list/",
        myproperty,
        setMyProperty,
        (element) => {
          myproperty.push(element);
          //console.log(element);
          setMyProperty([...myproperty]);
        }
      );
    }
    fetchdata();
  }, []);

  function handelChangeFdata(event) {
    // event.terget.name
    //console.log(event.target.name);
    //setFdata({ ...fdata, [event.target.name]: event.target.value });
    event.persist();
    setFdata((state) => {
      // console.log(event.target.name);
      let data = { ...state, [event.target.name]: event.target.value };

      for (const key in data) {
        fdata[key] = data[key];
      }
      //handelFiltering(null);
      return data;
    });
  }

  function handelFiltering(event) {
    //alert("filter");
    let burl = `api/property/list/?`;
    for (const key in fdata) {
      burl += `${key}=${fdata[key]}&`;
    }
    //console.log(burl);
    load_fatch_Data(
      "propertylist",
      burl,
      myproperty,
      setMyProperty,
      (element) => {
        //  console.log(element);

        let d = [];
        if (element.hasOwnProperty("results")) {
          element.results.forEach((ele) => {
            d.push(ele);
          });
          setMyProperty([...d]);
        }
      },
      true,
      true
    );
  }
  const [formats, setFormats] = React.useState(() => []);

  return (
    <div>
      <div className="search_bar cover-img">
        <div className="cover-title">টু-লেট্ এখন হাতের মুঠোয়</div>

        <div className="ifields">
          <ThemeProvider theme={theme}>
            <SimpleSelect
              key={"8285333#"}
              name="city"
              label="Citys"
              handelChangeFdata={handelChangeFdata}
              curr_value={fdata.city}
              op={allcitys}
            />
            <SimpleSelect
              key={"828987533#"}
              name="property_type"
              label="Property type"
              handelChangeFdata={handelChangeFdata}
              curr_value={fdata.property_type}
              op={allpTypes}
            />

            <RangeSlider
              rname="price"
              rval={fdata.price}
              handelChangeFdata={handelChangeFdata}
            />
            <SimpleSelect
              key={"8k89jdjod7533#"}
              name="bedroom"
              label="Bed rooms"
              handelChangeFdata={handelChangeFdata}
              curr_value={fdata.bedroom}
              op={
                [0].map(() => {
                  const d = [];
                  for (let i = 1; i < 5; i++) {
                    d.push({ val: i, inlineTxt: i });
                  }
                  d.push({ val: "5+", inlineTxt: "5+" });
                  return d;
                })[0]
              }
            />
            <SimpleSelect
              key={"8k898755k3#"}
              name="bathroom"
              label="Bath rooms"
              handelChangeFdata={handelChangeFdata}
              curr_value={fdata.bathroom}
              op={
                [0].map(() => {
                  const d = [];
                  for (let i = 1; i < 5; i++) {
                    d.push({ val: i, inlineTxt: i });
                  }
                  d.push({ val: "5+", inlineTxt: "5+" });
                  return d;
                })[0]
              }
            />

            <MultipleSelect
              name={"features"}
              label={"Features"}
              data={allfeatures}
              handelChangeFdata={handelChangeFdata}
              selectedFeature={fdata.features}
            />
          </ThemeProvider>
        </div>
        {/* <Fab  style={{background:"white",color:"#ea4e2f"}} onClick={()=>{window.location.assign("./property/list/")}}>
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-search" viewBox="0 0 16 16">
      <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
      </svg>
      </Fab> */}

        <Button variant="contained" color="secondary" onClick={handelFiltering}>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            className="bi bi-filter-left"
            viewBox="0 0 16 16"
          >
            <path d="M2 10.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5zm0-3a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5zm0-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5z" />
          </svg>
          Filter
        </Button>
      </div>
      <Container className="propertys_list">
        <div
          className=""
          style={{ marginBottom: "10px", marginTop: "10px", fontSize: "20px" }}
        >
          Our Featured Properties
        </div>

        {/* <div style={{ float: 'right',margin: '10px 0 10px 0'}}>

          <ToggleButtonGroup value={formats} onChange={handleFormat} aria-label="text formatting">
            <ToggleButton value="bold" aria-label="bold">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" className="bi bi-grid-3x2" viewBox="0 0 16 16">
                <path d="M0 3.5A1.5 1.5 0 0 1 1.5 2h13A1.5 1.5 0 0 1 16 3.5v8a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 0 11.5v-8zM1.5 3a.5.5 0 0 0-.5.5V7h4V3H1.5zM5 8H1v3.5a.5.5 0 0 0 .5.5H5V8zm1 0v4h4V8H6zm4-1V3H6v4h4zm1 1v4h3.5a.5.5 0 0 0 .5-.5V8h-4zm0-1h4V3.5a.5.5 0 0 0-.5-.5H11v4z" />
              </svg>
            </ToggleButton>
            <ToggleButton value="italic" aria-label="italic">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" className="bi bi-list-ol" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M5 11.5a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5z" />
                <path d="M1.713 11.865v-.474H2c.217 0 .363-.137.363-.317 0-.185-.158-.31-.361-.31-.223 0-.367.152-.373.31h-.59c.016-.467.373-.787.986-.787.588-.002.954.291.957.703a.595.595 0 0 1-.492.594v.033a.615.615 0 0 1 .569.631c.003.533-.502.8-1.051.8-.656 0-1-.37-1.008-.794h.582c.008.178.186.306.422.309.254 0 .424-.145.422-.35-.002-.195-.155-.348-.414-.348h-.3zm-.004-4.699h-.604v-.035c0-.408.295-.844.958-.844.583 0 .96.326.96.756 0 .389-.257.617-.476.848l-.537.572v.03h1.054V9H1.143v-.395l.957-.99c.138-.142.293-.304.293-.508 0-.18-.147-.32-.342-.32a.33.33 0 0 0-.342.338v.041zM2.564 5h-.635V2.924h-.031l-.598.42v-.567l.629-.443h.635V5z" />
              </svg>
            </ToggleButton>
            <ToggleButton value="underlined" aria-label="underlined">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" className="bi bi-caret-left-fill" viewBox="0 0 16 16">
                <path d="M3.86 8.753l5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z" />
              </svg>
            </ToggleButton>
            <ToggleButton value="color" aria-label="color" >
            <Button>

<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" className="bi bi-caret-right-fill" viewBox="0 0 16 16">
      <path d="M12.14 8.753l-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z" />
    </svg>
    
</Button>
            </ToggleButton>
            
          </ToggleButtonGroup>
        <ButtonGroup size="small" aria-label="small outlined button group">
          
          <Button>Two</Button>
          <Button>Three</Button>
        </ButtonGroup>
        </div> */}

        <Grid container spacing={3}>
          {myproperty.map((property) => {
            return (
              <Fade in={true} style={{ transitionDelay: "500ms" }}>
                <Grid item xs={12} sm={6} md={3}>
                  <div
                    className="card"
                    style={{ boxShadow: "-2px 2px 9px -3px #020202" }}
                  >
                    <img
                      src={`${property.img[0].timage}`}
                      height="200"
                      className="card-img-top"
                      alt="..."
                    ></img>
                    <div className="card-body">
                      <div className="card-text">
                        <h6>
                          <a
                            href={
                              api_server_url +
                              "property/details/" +
                              property.slug
                            }
                          >
                            {property.title}
                          </a>
                        </h6>
                        <p>
                          <i className="fa fa-map-marker"></i> {property.area},
                          {property.city}
                        </p>

                        <small>
                          <i className="fa fa-bed"></i>{" "}
                          <span id="bednumber" className="pe-2">
                            {property.bedroom} Beds
                          </span>
                          <i className="fa fa-bath"></i>
                          <span id="bathnumber" className="pe-2">
                            {property.bathroom} Baths
                          </span>
                          <i className="fa fa-th-large"></i>
                          <span id="area" className="pe-2">
                            {property.property_size} sqft
                          </span>
                        </small>
                      </div>
                    </div>
                    <div
                      className="card-footer"
                      style={{ backgroundColor: "#ffff" }}
                    >
                      <small className="text-muted fw-bold">
                        BDT{" "}
                        <span className="fs-5" style={{ color: "#ff653d" }}>
                          {property.price}
                        </span>{" "}
                        / MONTH
                      </small>
                    </div>
                  </div>
                </Grid>
              </Fade>
            );
          })}
        </Grid>
      </Container>
    </div>
  );
}

export default App;
