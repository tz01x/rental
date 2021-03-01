import React, { useEffect } from 'react';
import { makeStyles,createMuiTheme,ThemeProvider,colors } from '@material-ui/core/styles';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';

const theme = createMuiTheme({
  palette: {
    primary: {
      main:"#ea4e2f"
    }
  },
});
const useStyles = makeStyles((theme) => ({
  formControl: {
    margin: theme.spacing(1),
    minWidth: "300px",
    outlineColor:"#000000d1",
    

  },
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
  filled:{
    backgroundColor:"white",
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
    <ThemeProvider theme={theme}>
      <FormControl variant="filled" style={{backgroundColor:"white"}} className={classes.formControl}>
        <InputLabel id="demo-simple-select-label">{props.label}</InputLabel>
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
            return <MenuItem value={v.val}>{v.inlineTxt}</MenuItem>
          }):null}
          
          
        </Select>
      </FormControl>
      
      
      </ThemeProvider>
  );
}
