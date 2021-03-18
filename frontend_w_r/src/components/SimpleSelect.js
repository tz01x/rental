import React, { useEffect } from 'react';
import { makeStyles,colors } from '@material-ui/core/styles';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';

const useStyles = makeStyles((theme) => ({
  formControl: {
    margin: theme.spacing(1),
    minWidth: "118px",
    // maxWidth:"130px",
    outlineColor:"#000000d1",
    boxShadow:"-1px 3px 5px -3px"
    

  },
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
  filled:{
    backgroundColor:"#ffffffc9",
    "&.Mui-focused":{
      backgroundColor:"white"
    }
  }
}));

export default function SimpleSelect(props) {
  const classes = useStyles();
 

useEffect(()=>{
  console.log(props);
},[])
  return (
    
      <FormControl variant="filled"  className={classes.formControl}>
        <InputLabel id="demo-simple-select-label" style={{fontSize:"0.8rem"}}>{props.label}</InputLabel>
        <Select
          
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={props.curr_value}
          onChange={props.handelChangeFdata}
          name={props.name}
          label={props.label}
          className={classes.filled}

        >
          <MenuItem value="">
            <em>None</em>
          </MenuItem>
          {props.op?props.op.map((v,idx)=>{
            return <MenuItem key={v.val} value={v.val}>{v.inlineTxt}</MenuItem>
          }):null}
          
          
        </Select>
      </FormControl>
      
      
      
  );
}
