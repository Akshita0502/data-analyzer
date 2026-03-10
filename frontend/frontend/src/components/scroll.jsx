import {motion, useScroll, useTransform} from "framer-motion"
function Scroll(){
    const {scrollYProgress} = useScroll();
    const filter = useTransform(
        scrollYProgress,
        [0, 1],
        ["blur(0px)", "blur(10px)"]
);

return(
 
    <motion.div style={{ filter }}>
    </motion.div>

);
    
}
export default Scroll;