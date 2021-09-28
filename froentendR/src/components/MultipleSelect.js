import React from "react";

import { makeStyles, useTheme } from "@material-ui/core/styles";
import Input from "@material-ui/core/Input";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
import FormControl from "@material-ui/core/FormControl";

import ListItemText from "@material-ui/core/ListItemText";
import Select from "@material-ui/core/Select";
import Checkbox from "@material-ui/core/Checkbox";
import Chip from "@material-ui/core/Chip";

const useStyles = makeStyles((theme) => ({
  formControl: {
    borderTopRightRadius: 3,
    borderTopLeftRadius: 3,
    margin: theme.spacing(1),
    boxShadow: "-1px 3px 5px -3px",
    // minWidth: 120,
    minWidth: "150px",
    // maxWidth: "250px",
    backgroundColor: "#ffffffc9",
    // marginTop:"25px",
    "& .MuiSelect-root": {
      margin: "4px"
    },
    "&.MuiInputBase-root.Mui-focused": {
      backgroundColor: "white"
    }
  },
  colorPrimary: {
    color: "#ea4e2f"
  }
}));
function getStyles(name, personName, theme) {
  return {
    fontWeight:
      personName.indexOf(name) === -1
        ? theme.typography.fontWeightRegular
        : theme.typography.fontWeightMedium
  };
}
const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 250
    }
  }
};

export default function MultipleSelect(props) {
  const classes = useStyles();

  const handleChange = (event) => {
    event.target["name"] = props.name;

    props.handelChangeFdata(event);
  };

  return (
    <div>
      {/* <FormControl className={classes.formControl}>
        <InputLabel id="demo-mutiple-name-label">Name</InputLabel>
        <Select
          labelId="demo-mutiple-name-label"
          id="demo-mutiple-name"
          multiple
          value={personName}
          onChange={handleChange}
          
         
          MenuProps={MenuProps}
        >
          {names.map((name) => (
            <MenuItem key={name} value={name} >
              {name}
            </MenuItem>
          ))}
        </Select>
      </FormControl> */}

      <FormControl className={classes.formControl}>
        <InputLabel
          style={{ left: "12px", fontSize: "0.8rem" }}
          id="a-mutiple-checkbox-label"
        >
          {props.label ? props.label : null}
        </InputLabel>
        <Select
          labelId="a-mutiple-checkbox-label"
          id="a-mutiple-checkbox"
          multiple
          value={props.selectedFeature}
          onChange={handleChange}
          input={<Input />}
          renderValue={(selected) => selected.join(", ")}
          MenuProps={MenuProps}
        >
          {props.data.map((name) => (
            <MenuItem key={name} value={name}>
              <Checkbox
                className={classes.colorPrimary}
                checked={props.selectedFeature.indexOf(name) > -1}
              />
              <ListItemText primary={name} />
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </div>
  );
}
