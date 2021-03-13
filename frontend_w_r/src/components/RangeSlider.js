import React, { useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Slider from '@material-ui/core/Slider';
import Tooltip from '@material-ui/core/Tooltip';
import PropTypes from 'prop-types';
import Input from '@material-ui/core/Input';
import Grid from '@material-ui/core/Grid';
import { yellow } from '@material-ui/core/colors';

const useStyles = makeStyles((theme) => ({
    root: {
        minWidth: "295px",
        maxWidth: "315px",
        // height:"70px",
        margin: theme.spacing(1),
        

        // position:"relative",
        // left:"-100px",
        // top:"8px",
        backgroundColor:"#ffffffc9",
        boxShadow:"-1px 3px 5px -3px",



        //   display:flex,

    },
    margin: {
        height: theme.spacing(3),
    },
    input: {
        width: 80,
        height: "1.00em"
    },
    rlables: {
        
        fontSize: "12px",
        paddingLeft: "4%",
        paddingTop: "1.5%",
        color:"#757575",
        // top: "-25px",
        // left:"80px"
    }
}));
function ValueLabelComponent(props) {
    const { children, open, value } = props;

    return (
        <Tooltip open={open} enterTouchDelay={0} placement="top" title={value}>
            {children}
        </Tooltip>
    );
}

ValueLabelComponent.propTypes = {
    children: PropTypes.element.isRequired,
    open: PropTypes.bool.isRequired,
    value: PropTypes.number.isRequired,
};


export default function RangeSlider(props) {

    const classes = useStyles();
    const [values, setValue] = React.useState(['5000', '10000']);

    // const handleChange = (event, newValue) => {
    //     setValue(newValue);
    //     event.target['name'] = props.rname;
    //     event.target['value'] = props.newValue;
    //     props.handelChangeFdata(event);
    // };
    const handleInputChange = (event,inputname) => {
        //setValue(event.target.value === '' ? '' : Number(event.target.value));

        let tempnum=0;
        try {
            tempnum = Number(event.target.value);

            }catch{
                return;
            }
        // console.log(tempnum);
        // console.log(inputname);
        if (tempnum < 0) {
            // console.log("to small");
            return;
        }

        if (tempnum > 1e8) {
            // console.log("to big");

            return;
        }

        if (inputname== "maxval") {
            // console.log("change max val");
            setValue([values[0], tempnum.toString()]);

            event.target['name'] = props.rname;
            event.target['value'] = [Number(values[0]), tempnum];
            props.handelChangeFdata(event);
        }
        else if (inputname == "minval") {
            setValue([tempnum.toString(), values[1]]);
            event.target['name'] = props.rname;
            event.target['value'] = [tempnum, Number(values[1])];
            props.handelChangeFdata(event);

        }


    };
    // const handleBlur = () => {
    //     if (value[0] < 0) {
    //         setValue([0,value[1]]);
    //     } 
    //     if (value[1] <0) {
    //         setValue([value[0],0]);
    //     }
    // };
    useEffect(() => {

    });

    return (
        <div className={classes.root}>

            <Typography className={classes.rlables} id="range-slider">
                Price (<strong>BDT</strong>)
            </Typography>
            {/*
      <Slider
      ValueLabelComponent={ValueLabelComponent}
        value={value}
        onChange={handleChange}
        valueLabelDisplay="auto"
        aria-labelledby="range-slider"
        setp={1000}
        min={0}
        max={50000}
      /> */}

            <div style={{
                display: "flex",
                // alignItems: "baseline",
                justifyContent: "space-around",

                backgroundColor: yellow,
                position: "relative",
                // top:"-28px",
                left: "14px",
                top: "7px",
            }}>
                <Grid container spacing={1} alignItems="baseline">
                    <Grid item>
                        <p style={{ fontSize: 16 }}>Min</p>
                    </Grid>
                    <Grid item>
                        <Input

                            className={classes.input}
                            value={values[0]}
                            name="minval"
                            margin="dense"
                            onChange={(e)=>handleInputChange(e,"minval")}
                        // onBlur={handleBlur}

                        inputProps={{
                            step: 10,

                            type: 'number',
                            'aria-labelledby': 'input-slider',
                        }}
                        />
                    </Grid>
                </Grid>
                {/* <p style={{ fontSize: "26" }}>-</p> */}
                <Grid container spacing={1} alignItems="baseline">
                    <Grid item>
                        <p style={{ fontSize: 16 }}>Max</p>
                    </Grid>
                    <Grid item>
                        <Input

                            className={classes.input}
                            value={values[1]}
                            name="maxval"
                            margin="dense"

                            onChange={(e)=>handleInputChange(e,"maxval")}
                        // onBlur={handleBlur}
                        inputProps={{
                            step: 10,
                            type: 'number',
                            'aria-labelledby': 'input-slider',
                        }}
                        />
                    </Grid>
                </Grid>
            </div>

        </div>
    );
}
