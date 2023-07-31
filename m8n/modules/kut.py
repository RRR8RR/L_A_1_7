import random
from pyrogram import Client, filters
from pyrogram.types import Message

from m8n import app
from m8n.config import que

from m8n.utils.filters import command, other_filters
from m8n.utils.decorators import sudo_users_only
from m8n.tgcalls.queues import clear, get, is_empty, put, task_done


Citation1_morning = [
    "** أكثر شيء يُسكِت الطفل برأيك؟ **",
    "** تخيّل لو أنك سترسم شيء وحيد فيصبح حقيقة، ماذا سترسم؟ **",
    "** قناة الكرتون المفضلة في طفولتك ؟ **",
    "** الحرية لـ ... ؟ **",
    "** كلمة للصُداع؟ **",
    "** ما الشيء الذي يُفارقك؟ **",
    "** ما الشيء الذي يُفارقك؟ **",
    "** موقف مميز فعلته مع شخص ولايزال يذكره لك؟ **",
    "** أيهما ينتصر، الكبرياء أم الحب؟ **",
    "** كت تويت | بعد ١٠ سنين شنو تصير ؟ **",
    "** مِن أغرب وأجمل الأسماء التي مرت عليك؟ **",
    "** عمرك شلت مصيبة عن شخص برغبتك ؟ **",
    "** أكثر سؤال وجِّه إليك مؤخرًا؟ **",
    "** ما هو الشيء الذي يجعلك تشعر بالخوف؟ **",
    "** شنو الي يفسد الصداقة؟ **",
    "** شخص لاترفض له طلبا ؟ **",
    "** كم مره خسرت شخص تحبه؟ **",
    "** كيف تتعامل مع الاشخاص السلبيين ؟ **",
    "** كلمة تشعر بالخجل اذا قيلت لك؟ **",
    "** جسمك اكبر من عٌمرك او العكسّ ؟ **",
    "** أقوى كذبة مشت عليك ؟ **",
    "** تتأثر بدموع شخص يبكي قدامك قبل تعرف السبب ؟ **",
    "** هل حدث وضحيت من أجل شخصٍ أحببت؟ **",
    "** أكثر تطبيق تستخدمه مؤخرًا؟ **",
    "** ‏اكثر شي يرضيك اذا زعلت بدون تفكير ؟ **",
    "** شنو محتاج حتى تكون مبسوط ؟ **",
    "** مطلبك الوحيد الحين ؟ **",
    "** هل حدث وشعرت بأنك ارتكبت أحد الذنوب أثناء الصيام؟ **",
    "** اكثر مطور تحبه برنثون منو ؟ **",
    "** من هو الممثل المفضل لديك؟ **",
    "** من ستختار من بين الموجودين ليمسح دموعك ويخفف أحزانك؟ **",
    "** إذا رأيتِ أحد أجمل منكِ هل يمكن أن تشعري بالغيرة منها؟ **",
    "** كم علبة سجائر تقوم بتدخينها يومياً؟ **",
    "** هل أنت شخصية مغرورة؟ **",
    "** كم ساعة تقضيها على الإنترنت يومياً؟ **",
    "** ما هي عادتك اليومية المفضلة؟ **",
    "** ما هي العادة اليومية التي تقوم بها وتكرهها وتريد تغييرها؟ **",
    "** هل تخبر صديقك بكل أسرارك أم تحتفظ ببضع منها لنفسك؟ **",
    "** كيف ستتصرف إن قام صديقك المقرب بالابتعاد عنك بدون سبب؟ **",
    "** أي سنة من سنين حياتك كانت الأجمل، وما الذي حدث فيها؟ **",
    "** من الشخص الذي تحلم به كثيرًا عندما تنام؟ **",
    "** هل قمت بالكذب على أصدقائك من قبل ، ولماذا؟ **",
    "** هل أنت شخص عنيد؟ **",
    "** من الصديق الذي ستأخذه معه عند سفرك لقضاء عطلتك في أي بلد بعيدة؟ **",
    "** من هو آخر شخص تقوم بالتفكير فيه قبل نومك؟ **",
      "اكثر شي ينرفزك .. ؟!",
  "اخر مكان رحتله ..؟!",
  "سـوي تـاك @ لـ شخص تريـد تعترفلـه بشي ؟",
  "تغار ..؟!",
  "هـل تعتقـد ان في أحـد يراقبـك 👩🏼‍💻..؟!",
  "أشخاص ردتهم يبقون وياك ومن عرفو هلشي سوو العكس صارت معك؟",
  "ولادتك بنفس المكان الي هسة عايش بي او لا؟",
  "اكثر شي ينرفزك ؟",
  "تغار ؟",
  "كم تبلغ ذاكرة هاتفك؟",
  "صندوق اسرارك ؟",
  "شخص @ تعترفلة بشي ؟",
  "يومك ضاع على ؟",
  "اغرب شيء حدث في حياتك ؟",
  " نسبة حبك للاكل ؟",
  " حكمة تأمان بيها ؟",
  " اكثر شي ينرفزك ؟",
  " هل تعرضت للظلم من قبل؟",
  " خانوك ؟",
  " تزعلك الدنيا ويرضيك ؟",
  " تاريخ غير حياتك ؟",
  " أجمل سنة ميلادية مرت عليك ؟",
  " ولادتك بنفس المكان الي هسة عايش بي او لا؟",
  " تزعلك الدنيا ويرضيك ؟",
  " ماهي هوايتك؟",
  " دوله ندمت انك سافرت لها ؟",
  "شخص اذا جان بلطلعة تتونس بوجود؟",
  " تاخذ مليون دولار و تضرب خويك؟",
  " تاريخ ميلادك؟",
  "اشكم مره حبيت ؟",
  " يقولون ان الحياة دروس ، ماهو أقوى درس تعلمته من الحياة ؟",
  " هل تثق في نفسك ؟",
  " كم مره نمت مع واحده ؟",
  " اسمك الثلاثي ؟",
  "كلمة لشخص خذلك؟",
  "هل انت متسامح ؟",
  "طريقتك المعتادة في التخلّص من الطاقة السلبية؟",
  "عصير لو قهوة؟",
  " صديق أمك ولا أبوك. ؟",
  "تثق بـ احد ؟",
  "كم مره حبيت ؟",
  "اكمل الجملة التالية..... قال رسول الله ص،، انا مدينة العلم وعلي ؟",
  " اوصف حياتك بكلمتين ؟",
  " حياتك محلوا بدون ؟",
  " وش روتينك اليومي؟",
  " شي تسوي من تحس بلملل؟",
  " يوم ميلادك ؟",
  " اكثر مشاكلك بسبب ؟",
  " تزعلك الدنيا ويرضيك ؟",
  " تتوقع فيه احد حاقد عليك ويكرهك ؟",
  "كلمة غريبة من لهجتك ومعناها؟",
"   هل تحب اسمك أو تتمنى تغييره وأي الأسماء ستختار" ,
"  كيف تشوف الجيل ذا؟",
"  تاريخ لن تنساه📅؟",
"  هل من الممكن أن تقتل أحدهم من أجل المال؟",
"  تؤمن ان في حُب من أول نظرة ولا لا ؟.",
"  ‏ماذا ستختار من الكلمات لتعبر لنا عن حياتك التي عشتها الى الآن؟💭",
"  طبع يمكن يخليك تكره شخص حتى لو كنت تُحبه🙅🏻‍♀️؟",
"  ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",
"  أطول مدة نمت فيها كم ساعة؟",
"  كلمة غريبة من لهجتك ومعناها؟🤓",
"  ردة فعلك لو مزح معك شخص م تعرفه ؟",
"  شخص تحب تستفزه😈؟",
"  تشوف الغيره انانيه او حب؟",
"  مع او ضد : النوم افضل حل لـ مشاكل الحياة؟",
"  اذا اكتشفت أن أعز أصدقائك يضمر لك السوء، موقفك الصريح؟",
"  ‏للشباب | آخر مرة وصلك غزل من فتاة؟🌚",
"  أوصف نفسك بكلمة؟",
"  شيء من صغرك ماتغير فيك؟",
"  ردة فعلك لو مزح معك شخص م تعرفه ؟",
"  | اذا شفت حد واعجبك وعندك الجرأه انك تروح وتتعرف عليه ، مقدمة الحديث شو راح تكون ؟.",
"  كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",
"  حاجة تشوف نفسك مبدع فيها ؟",
"  يهمك ملابسك تكون ماركة ؟",
"  يومك ضاع على؟",
"  اذا اكتشفت أن أعز أصدقائك يضمر لك"," السوء، موقفك الصريح؟",
"  هل من الممكن أن تقتل أحدهم من أجل المال؟",
"  كلمه ماسكه معك الفترة هذي ؟",
"  كيف هي أحوال قلبك؟",
"  صريح، مشتاق؟",
"  اغرب اسم مر عليك ؟",
"  تختار أن تكون غبي أو قبيح؟",
"  آخر مرة أكلت أكلتك المفضّلة؟",
"  دوله ندمت انك سافرت لها😁؟",
"  اشياء صعب تتقبلها بسرعه ؟",
"  كلمة لشخص غالي اشتقت إليه؟💕",
"  اكثر شيء تحس انه مات ف مجتمعنا؟",
"  هل يمكنك مسامحة شخص أخطأ بحقك لكنه قدم الاعتذار وشعر بالندم؟",
"  آخر شيء ضاع منك؟",
"  تشوف الغيره انانيه او حب؟",
"  لو فزعت/ي لصديق/ه وقالك مالك دخل وش بتسوي/ين؟",
"  شيء كل م تذكرته تبتسم ...",
"  هل تحبها ولماذا قمت باختيارها؟",
"  هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
"  متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",
"  أقبح القبحين في العلاقة: الغدر أو الإهمال🤷🏼؟", 
"  هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",
"  هل تشعر أن هنالك مَن يُحبك؟",
"  وش الشيء الي تطلع حرتك فيه و زعلت ؟",
"  صوت مغني م تحبه",
"  كم في حسابك البنكي ؟",
"  اذكر موقف ماتنساه بعمرك؟",
"  ردة فعلك لو مزح معك شخص م تعرفه ؟",
"  عندك حس فكاهي ولا نفسية؟",
"  من وجهة نظرك ما هي الأشياء التي تحافظ على قوة وثبات العلاقة؟",
"  ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",
"  هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
"  هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",
"  شيء من صغرك ماتغير فيك؟",
"  هل يمكنك أن تضحي بأكثر شيء تحبه وتعبت للحصول عليه لأجل شخص تحبه؟",
"  هل تحبها ولماذا قمت باختيارها؟",
"  لو فزعت/ي لصديق/ه وقالك مالك دخل وش بتسوي/ين؟",
"  كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",
"  كم مره تسبح باليوم",
"  أفضل صفة تحبه بنفسك؟",
"  أجمل شيء حصل معك خلال هاليوم؟",
"  ‏شيء سمعته عالق في ذهنك هاليومين؟",
"  هل يمكنك تغيير صفة تتصف بها فقط لأجل شخص تحبه ولكن لا يحب تلك الصفة؟",
"  ‏أبرز صفة حسنة في صديقك المقرب؟",
"  ما الذي يشغل بالك في الفترة الحالية؟",
"  آخر مرة ضحكت من كل قلبك؟",
"  احقر الناس هو من ...",
"  اكثر دوله ودك تسافر لها🏞؟",
"  آخر خبر سعيد، متى وصلك؟",
"  ‏نسبة احتياجك للعزلة من 10📊؟",
"  هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
"  أكثر جملة أثرت بك في حياتك؟",
"  لو قالوا لك  تناول صنف واحد فقط من الطعام لمدة شهر .",
"  هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
"  آخر مرة ضحكت من كل قلبك؟",
"  وش الشيء الي تطلع حرتك فيه و زعلت ؟",
"  تزعلك الدنيا ويرضيك ؟",
"  متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",
"  تعتقد فيه أحد يراقبك👩🏼‍💻؟",
"  احقر الناس هو من ...",
"  شيء من صغرك ماتغير فيك؟",
"  وين نلقى السعاده برايك؟",
"  هل تغارين من صديقاتك؟",
"  أكثر جملة أثرت بك في حياتك؟",
"  كم عدد اللي معطيهم بلوك👹؟",
"  أجمل سنة ميلادية مرت عليك ؟",
"  أوصف نفسك بكلمة؟",
]



@app.on_message(command(["كت", f"كت تويت"]) & other_filters)

async def kut(client, message: Message):

rnthon = random.choice(Citation1_morning)
    await message.reply(f"{rnthon}")